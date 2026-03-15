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

### Vercel (recommended)

Use the current repository directly.

The repository root includes a minimal `vercel.json` that pins the framework, install command, build command, and output directory for the `site/` app. You still need to set the Vercel project Root Directory to `site`.

Project settings:

- Framework Preset: `Vite`
- Root Directory: `site`
- Build Command: `npm run build`
- Output Directory: `dist`

Recommended flow:

1. Push the repository to GitHub.
2. Import the repository into Vercel.
3. Set the Root Directory to `site`.
4. Confirm the detected settings still show `npm install`, `npm run build`, and `dist`.
5. Deploy.

### Important data note

The current leaderboard data is bundled at build time from `leaderboard/output/preview-leaderboard.json`. That means each deployment reflects whatever leaderboard artifact exists in the repo at build time.

### Generic static hosting

1. Regenerate `leaderboard/output/preview-leaderboard.json` when the benchmark snapshot changes.
2. Run `npm run build` in `site/`.
3. Deploy the contents of `site/dist/` to any static host.

Suitable targets include Vercel, Netlify, GitHub Pages, Cloudflare Pages, or any CDN/object storage setup that serves `index.html` plus the `assets/` directory.
