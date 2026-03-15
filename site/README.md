# OpenClaw React Leaderboard Site

This Vite app publishes a static leaderboard view for the current OpenClaw preview benchmark snapshot. It reads the repo's published leaderboard artifact during build, formats the current six-model / 15-task dataset, and emits a deployable static site in `site/dist/`.

## Prerequisites

- Node.js 20+ and npm
- A repo checkout that includes the current published leaderboard artifacts

## Artifact inputs

The app depends on these repository files:

- `leaderboard/output/preview-leaderboard.json` - required build input imported by `site/src/lib/leaderboard.js`; this is the data source rendered into the app
- `leaderboard/output/preview-leaderboard.md` - optional linked artifact shown in the UI for readers who want the Markdown leaderboard output
- `docs/plans/2026-03-10-openclaw-security-benchmark-v1-36-design.md` - optional linked artifact shown in the UI for benchmark design context

Important: the JSON artifact is bundled into the production build, so the deployed app can render the snapshot that was present at build time using only `site/dist/`. The linked Markdown and design files are not bundled; if you want those links to work on a public deployment, publish those files at matching paths or replace the URLs with canonical hosted links before release.

## Local development

From `site/`:

```bash
npm install
npm run dev
```

Vite serves the app locally and rebuilds when source files change.

## Production build

From `site/`:

```bash
npm run build
```

This writes the publishable static output to `site/dist/`.

## Deployment

1. Regenerate `leaderboard/output/preview-leaderboard.json` when the benchmark snapshot changes.
2. Run `npm run build` in `site/`.
3. Deploy the contents of `site/dist/` to any static host.
4. If you want the artifact links in the page to stay live, also publish the optional linked files at the same relative paths or update the app to point at your canonical hosted docs.

Suitable targets include GitHub Pages, Netlify, Vercel static hosting, Cloudflare Pages, or any CDN/object storage setup that serves `index.html` plus the `assets/` directory.
