import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from pet_assets import ROOT, build_from_frames, load_manifest, validate_image

class AssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = load_manifest()

    def test_frames_reproduce_published_pixels(self):
        rebuilt = build_from_frames(self.manifest)
        with Image.open(ROOT/self.manifest['spritesheet']) as saved:
            self.assertEqual(rebuilt.tobytes(), saved.tobytes())

    def test_rejects_unused_cell_artwork(self):
        atlas = build_from_frames(self.manifest)
        atlas.putpixel((7*192+96,100),(255,0,0,255))
        with self.assertRaisesRegex(ValueError,'Unused cell'):
            validate_image(atlas)

    def test_rejects_missing_frame(self):
        atlas = build_from_frames(self.manifest)
        atlas.paste(Image.new('RGBA',(192,208)),(0,0))
        with self.assertRaisesRegex(ValueError,'Required cell.*empty'):
            validate_image(atlas)

    def test_rejects_clipping(self):
        atlas = build_from_frames(self.manifest)
        atlas.putpixel((0,100),(255,255,255,255))
        with self.assertRaisesRegex(ValueError,'touches the edge'):
            validate_image(atlas)

    def test_rejects_escaping_source_path(self):
        bad = copy.deepcopy(self.manifest)
        bad['rows'][0]['frames'][0] = '../external.png'
        with self.assertRaisesRegex(ValueError,'inside the repository'):
            build_from_frames(bad)

    def test_rejects_wrong_geometry(self):
        with self.assertRaisesRegex(ValueError,'1536x2288'):
            validate_image(Image.new('RGBA',(1536,1872)))

    def test_rejects_wrong_manifest_frame_count(self):
        bad = copy.deepcopy(self.manifest)
        bad['rows'][4]['frames'].pop()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'pet.json').write_text(json.dumps(bad))
            with self.assertRaisesRegex(ValueError,'Incorrect frame count'):
                load_manifest(root)

if __name__ == '__main__':
    unittest.main()
