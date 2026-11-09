# Sprite format

The v2 sheet is a transparent 1536 × 2288 PNG: eight columns and eleven rows of 192 × 208 cells. Rows 0–8 contain 6, 8, 8, 4, 5, 8, 6, 6, and 6 frames. Rows 9–10 contain eight look poses each. All 15 unused cells remain transparent.

The sixteen look poses run clockwise from up: 0°, 22.5°, 45°, 67.5°, 90°, 112.5°, 135°, 157.5°, 180°, 202.5°, 225°, 247.5°, 270°, 292.5°, 315°, 337.5°. Coordinates are viewer-relative: 90° is screen-right and 270° is screen-left. The neutral resting pose belongs to idle, not to the sixteen-direction sweep.

Marvin’s lens shapes are fixed parts of his head. Looking around uses head pitch and yaw while keeping his body and feet anchored. There are no movable pupils or added human facial features.

`pet.json` describes the cell order and local-preview durations. The PNG stores pixels only; preview durations do not configure the Pets host.
