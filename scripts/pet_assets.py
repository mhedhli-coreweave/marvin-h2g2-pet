"""Portable assembly of approved pet frames; no image generation or account access."""
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CELL = (192, 208)
COUNTS = (6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8)
SIZE = (1536, 2288)


def load_manifest(root=ROOT):
    manifest = json.loads((root / "pet.json").read_text(encoding="utf-8"))
    if (manifest["cell_width"], manifest["cell_height"]) != CELL:
        raise ValueError("Expected 192x208 cells")
    if manifest["sprite_version"] != 2 or manifest["columns"] != 8:
        raise ValueError("Expected an eight-column v2 sprite sheet")
    rows = manifest["rows"]
    if len(rows) != len(COUNTS):
        raise ValueError("Expected eleven rows")
    for index, (row, count) in enumerate(zip(rows, COUNTS)):
        if row["row"] != index or len(row["frames"]) != count:
            raise ValueError(f"Incorrect frame count or position for row {index}")
        if len(row["durations_ms"]) != count or any(d <= 0 for d in row["durations_ms"]):
            raise ValueError(f"Invalid preview durations for row {index}")
    return manifest


def build_from_frames(manifest, root=ROOT):
    atlas = Image.new("RGBA", SIZE)
    for row in manifest["rows"]:
        for column, filename in enumerate(row["frames"]):
            path = (root / filename).resolve()
            if not path.is_relative_to(root.resolve()):
                raise ValueError("Frame paths must remain inside the repository")
            with Image.open(path) as frame:
                if frame.size != CELL or frame.mode != "RGBA":
                    raise ValueError(f"Expected an RGBA 192x208 frame: {filename}")
                # No scaling, filtering, recoloring or alpha re-compositing.
                atlas.paste(frame, (column * CELL[0], row["row"] * CELL[1]))
    validate_image(atlas)
    return atlas


def validate_image(atlas):
    """Check local grid/transparency integrity; Pets still owns upload validation."""
    if atlas.size != SIZE or atlas.mode != "RGBA":
        raise ValueError("Expected a 1536x2288 RGBA v2 sprite sheet")
    for row, count in enumerate(COUNTS):
        for column in range(8):
            alpha = atlas.crop((column*192, row*208, (column+1)*192, (row+1)*208)).getchannel("A")
            bounds = alpha.getbbox()
            if column >= count:
                if bounds is not None:
                    raise ValueError(f"Unused cell {row}:{column} contains pixels")
            elif bounds is None:
                raise ValueError(f"Required cell {row}:{column} is empty")
            elif alpha.getextrema()[0] != 0:
                raise ValueError(f"Required cell {row}:{column} has no transparent background")
            elif bounds[0] == 0 or bounds[1] == 0 or bounds[2] == 192 or bounds[3] == 208:
                raise ValueError(f"Artwork touches the edge of cell {row}:{column}")


def fail_cleanly(main):
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error)) from error
