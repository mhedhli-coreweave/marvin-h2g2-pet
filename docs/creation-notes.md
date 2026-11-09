# Creation notes

## Brief

Create Marvin from the newer adaptation of *The Hitchhiker’s Guide to the Galaxy*, guided by the two user-supplied images. A stylized 3D toy rendering was selected for clarity at desktop-pet scale. Preserve the oversized spherical head, pearl-white armor, black joints and hands, fixed green triangular lenses, and small cyan chest indicator.

Marvin’s personality is expressed through hesitant gestures, heavy feet, slumped shoulders, and head pitch. No human mouth, eyebrows, pupils, or tears were added. No floating icons or scene props appear in the frames.

## Source workflow

A canonical base was generated first. Each of the nine action strips was generated separately from that base and the identity references. The leftward gait was generated independently to retain screen-fixed lighting. The four cardinal head poses anchored two coherent eight-frame direction strips.

The bundled Pets pipeline extracted connected pose groups with shared row scale. Stationary poses were registered by the planted feet. Non-jump rows were reduced together to reserve airborne headroom; the jump retained its original vertical displacement. The final sheet received one chroma-edge cleanup pass.

The repository’s `source/` folder contains the selected generated base and strips. `prompts/` records the generation instructions, with local source paths omitted. Source images still have a magenta extraction background; the final sheet and approved cells are transparent.

## Reproducibility boundary

Approved final frame PNGs deterministically rebuild the published sheet, pixel for pixel. Regenerating artwork from the prompts is nondeterministic and requires fresh visual review. The small repository validator checks grid integrity only and does not replace the full Pets creation pipeline, semantic direction review, or service preflight.
