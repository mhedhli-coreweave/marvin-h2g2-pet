# Validation

Validated on 2026-11-09 against the exact published PNG. The checksum is recorded in `asset-checksums.json`.

- The bundled Pets v2 atlas validator passed: 1536 × 2288 RGBA PNG, 73 populated cells, 15 transparent unused cells, 1,990,118 bytes, no structural or chroma errors.
- Every standard row passed bundled connected-component/frame inspection.
- One final chroma-edge cleanup pass preserved alpha and cleared hidden transparent RGB.
- The quality gate passed. The hop lifts 33 pixels and lands on the idle baseline. Maximum horizontal gaze drift is 1 pixel, and look silhouette widths vary by about 5%.
- Sixteen directions were visually reviewed. Three independent blind reviewers agreed on all four cardinals and all vertical comparisons. Four near-vertical poses (22.5°, 157.5°, 202.5°, 337.5°) have subtle horizontal yaw that was ambiguous in isolated blind pairs. These remain reviewed warnings: the complete arc is coherent and no wrong-quadrant pose or reversal was observed.
- Three adjacent pixel-difference outliers were visually reviewed. Adjacent bounding centers move by at most 1.81 pixels and visible area varies by less than 2%; no clipping or broken body anchors were observed.
- The Pets service preflight returned `valid: true`. Creation succeeded, and downloaded stored pixels matched the validated sheet exactly after decoding.
- The interactive preview was checked at desktop and 390-pixel mobile width. State selection, playback, pause, frame stepping, and keyboard cardinal navigation worked; no browser console warnings or errors were observed.
- The approved frame sources rebuild the published PNG pixel for pixel. Seven unit tests passed, including missing cells, unused-cell contamination, clipping, path containment, geometry, and manifest frame counts.

The `qa/` reports retain the actual quality-gate warnings. Private account metadata and expiring service URLs are excluded from the repository.

The portable repository validator checks layout integrity. It does not independently judge character identity, motion semantics, direction meaning, or the host’s playback behavior.
