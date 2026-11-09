#!/usr/bin/env python3
"""Rebuild the sprite sheet, from approved frame PNGs."""
import argparse
from pathlib import Path
from PIL import Image
from pet_assets import (ROOT, build_from_frames, fail_cleanly,
                        load_manifest, validate_image)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="PNG destination; also the comparison file for --check")
    parser.add_argument("--check", action="store_true", help="Verify exact pixels without writing")
    args = parser.parse_args()
    manifest = load_manifest()
    output = args.output or ROOT/manifest["spritesheet"]
    rebuilt = build_from_frames(manifest)
    if args.check:
        with Image.open(output) as published:
            validate_image(published)
            if rebuilt.tobytes() != published.tobytes():
                raise ValueError(f"Source frames differ from {output}; rebuild and review the changes")
        print(f"PASS: Approved frame selection reproduces {output.name} pixel-for-pixel")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        rebuilt.save(output, format="PNG")
        print(f"Wrote {output}")


if __name__ == "__main__":
    fail_cleanly(main)
