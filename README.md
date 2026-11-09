# Marvin

A softly rendered 3D companion inspired by the newer movie adaptation of Marvin the Paranoid Android from *The Hitchhiker’s Guide to the Galaxy*. Huge pearl-white head, green triangular lenses, heavy feet, and very little enthusiasm.

![Marvin animation preview](assets/previews/all-states.gif)

## Personality and motion

| State | Motion |
| --- | --- |
| Idle | A small, weary sigh and head droop |
| Moving right / left | Slow, heavy-footed shuffle |
| Greeting | Reluctant raised hand and limp wave |
| Jump | A small hop that seems like far too much effort |
| Failed | Defeated facepalm |
| Waiting | An expectant, unimpressed palm-up gesture |
| Working | Weary concentration |
| Review | Skeptical inspection |
| Looking around | Sixteen head directions with the body anchored |

Open the local preview to try each state, step through frames, and move the pointer around Marvin. Preview timing is stored in `pet.json`; the Pets host controls its own playback timing.

## Preview locally

```sh
python3 -m http.server 8080
```

Open <http://localhost:8080>. The preview has no external dependencies or analytics.

## Rebuild and check

Requires Python 3.10+.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/render_previews.py --mp4
```

`build.py` assembles the approved frame PNGs without resizing, filtering, or changing pixels. Use `--output build/spritesheet.png` to write a new copy. GIF and MP4 previews go to `build/previews` by default.

## Use as a ChatGPT Pet

The ready-to-use sheet is [`assets/spritesheet.png`](assets/spritesheet.png). Ask the Pets plugin to create a pet from that file; it must validate the exact file before upload. This repository does not store account identifiers, upload sessions, or credentials.

The local validator checks grid integrity, transparency, and bounds. The creation workflow also used the Pets bundled visual-quality pipeline and service preflight. See [validation](docs/validation.md), [format](docs/animation-format.md), and [attribution](ATTRIBUTION.md).
