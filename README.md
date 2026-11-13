# Make the cutest picture — baby red panda with a strawberry

Entry for make.fun bounty [cutest-picture-01](https://make.fun/bounty/cutest-picture-01)
($250, deadline 2026-11-13 10:00 UTC).

## What it is

A photorealistic portrait of a baby red panda cub wearing a tiny pink flower
crown, head tilted, holding a ripe strawberry in both paws against a soft
pastel bokeh background. Built to the judge's criteria: cute at one glance,
big glossy eyes, chubby proportions, a head tilt plus a tiny accessory for
charm, clean rendering with correct anatomy, and a subject that still reads
clearly at ~300 px wide.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled picture to
the output directory. It uses no network and is fully deterministic — two
runs write byte-identical files.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (JPEG data, 1024x1024, ~172 KB — within the 1 MiB cap)
```

In the grader's container the output goes to `/output/entry.png`.

## Files

- `main.py` — the entrypoint, copies `entry.png` to the output directory
- `entry.png` — the picture (JPEG bytes, 1024x1024)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the payout wallet
- `candidates/` — the two unused alternate pictures (seal pup, kitten + red
  panda cuddle) are kept for reference in
  `~/workspace/makefun/cutest-picture-assets/candidates/`; they are not part
  of the entry

## Still needed before submit (parent agent)

- Create the public GitHub repo under Ervan1702 (created after the bounty
  opened 2026-11-12 10:00 UTC) and commit these files under the user's own
  git identity.
- Bundle the build transcripts (`makefun bundle`) and run the kit's
  `check` command.
- Sign the entry message with the Solana wallet that owns the payout
  address in `.makefun/owner.json` and submit before 2026-11-13 10:00 UTC.
