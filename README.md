# FixMyVibe

Plain-English fixes for broken vibe-coded apps. Live at [fixmyvibe.org](https://fixmyvibe.org).

## How it's built

- `content/fixes/` — one Markdown file per error. This is the fix library.
- `data/keywords.json` — extra phrases Error Doctor uses to match a pasted error to a fix.
- `assets/` — stylesheet and favicon.
- `build.py` — turns the above into a static site in `public/`.
- `public/` — the built site. This is what gets deployed, so it is committed.

## Adding or editing a fix

1. Add or edit a file in `content/fixes/` (copy an existing one for the format).
2. Add matching phrases for it in `data/keywords.json`.
3. Run `python3 build.py` (needs `pip install markdown pyyaml`).
4. Commit everything, including `public/`. The host redeploys on push.

## Hosting

`vercel.json` tells Vercel to serve `public/` with no build step. On Netlify or Cloudflare Pages, set the output directory to `public` and leave the build command empty.
