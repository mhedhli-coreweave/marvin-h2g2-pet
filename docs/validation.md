# Validation

Validated on 2026-11-09 against the exact published More angst PNG. Both variant checksums are recorded in `asset-checksums.json`.

- The bundled Pets v2 atlas validator passed: 1536 × 2288 RGBA PNG, 73 populated cells, 15 transparent unused cells, 2,034,226 bytes, no structural or chroma errors.
- Every newly generated standard row passed bundled connected-component/frame inspection. Visual review confirmed held gestures, clear direction of travel, planted feet, and the review action's point, squint, and alternating head yaw.
- All nine action rows include lit and unlit eye frames. `qa/eye-light-audit.json` records green-pixel counts; visual inspection confirms dark triangular lenses and facepalm occlusion.
- One final chroma-edge cleanup pass preserved alpha and cleared hidden transparent RGB. The final sixteen gaze cells are pixel-identical to the original published sheet.
- The quality gate passed. The hop lifts 29 pixels and lands within 1 pixel of the idle baseline. Maximum horizontal gaze drift is 1 pixel, and look silhouette widths vary by about 5%.
- Three independent blind reviewers confirmed all four cardinal directions and all vertical comparisons. Four near-vertical poses (22.5°, 157.5°, 202.5°, 337.5°) retain ambiguous horizontal yaw in isolated pairs. These are reviewed warnings in the unchanged gaze artwork. No wrong-quadrant pose or reversal was observed in the full arc.
- Three adjacent gaze pixel-difference outliers remain reviewed warnings. Adjacent bounding centers move by at most 1.81 pixels and visible area varies by less than 2%; no clipping or broken body anchors were observed.
- The Pets service preflight returned `valid: true`. The existing pet was updated, remained active, and downloaded stored pixels matched the validated sheet exactly after decoding.
- The interactive preview was checked at desktop and 390-pixel mobile width. Both animation sets, variant-specific download links, playback, pause, frame stepping, and keyboard direction selection worked. No browser console warnings or errors were observed.
- Both sets rebuild pixel for pixel. Nine unit tests passed, including original-set preservation, unknown variants, missing cells, unused-cell contamination, clipping, path containment, geometry, and manifest frame counts.

The `qa/` reports retain the actual quality-gate warnings. The original reports remain under `variants/original/qa/`. Private account metadata and expiring service URLs are excluded from the repository.

The portable repository validator checks layout integrity. It does not independently judge character identity, motion semantics, direction meaning, or the host's playback timing.
