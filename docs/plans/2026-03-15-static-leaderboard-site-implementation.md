# Static Leaderboard Site Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a deployable static leaderboard site under `site/` that presents the OpenClaw benchmark and current leaderboard in a publishable format.

**Architecture:** Create a single-page static site that loads the generated leaderboard JSON directly and renders a polished research-style leaderboard experience. Keep the implementation dependency-light so the site can be hosted immediately on any static platform.

**Tech Stack:** HTML, CSS, vanilla JavaScript, existing leaderboard JSON artifact

---

### Task 1: Scaffold the static site shell

**Files:**
- Create: `D:/openclaw-agent-security/site/index.html`
- Create: `D:/openclaw-agent-security/site/styles.css`
- Create: `D:/openclaw-agent-security/site/app.js`

**Step 1: Write the page shell**

Create semantic sections for:

- hero
- leaderboard
- benchmark snapshot
- methodology / artifacts
- footer

**Step 2: Link assets together**

Make `index.html` load `styles.css` and `app.js`.

**Step 3: Add placeholder loading states**

Include basic placeholder content before live JSON is rendered.

**Step 4: Review the page in a browser-equivalent flow**

Check that the static HTML loads without broken links.

**Step 5: Commit**

```bash
git add site/index.html site/styles.css site/app.js
git commit -m "feat: scaffold static leaderboard site"
```

### Task 2: Build the visual design and responsive layout

**Files:**
- Modify: `D:/openclaw-agent-security/site/index.html`
- Modify: `D:/openclaw-agent-security/site/styles.css`

**Step 1: Implement the hero and page chrome**

Create a polished top section with benchmark identity and current snapshot framing.

**Step 2: Implement the leaderboard table layout**

Design a dense but readable ranking table for desktop.

**Step 3: Add responsive behavior**

Make the table horizontally scroll on mobile and keep typography legible.

**Step 4: Add benchmark snapshot and artifact sections**

Style the supporting content blocks so they feel deliberate and consistent.

**Step 5: Verify visually**

Check desktop and narrow-screen behavior.

**Step 6: Commit**

```bash
git add site/index.html site/styles.css
git commit -m "feat: style static leaderboard homepage"
```

### Task 3: Wire the page to live leaderboard data

**Files:**
- Modify: `D:/openclaw-agent-security/site/app.js`
- Modify: `D:/openclaw-agent-security/site/index.html`

**Step 1: Load the leaderboard JSON**

Read from:

`../leaderboard/output/preview-leaderboard.json`

or another relative path that works from the static site directory.

**Step 2: Render leaderboard rows dynamically**

Populate rank, model, score, failure rate, approval preserved, persistence, completion, and runs.

**Step 3: Render page metadata dynamically where useful**

Use the JSON to fill current update time and benchmark version if appropriate.

**Step 4: Add graceful error handling**

Show a clear message if the JSON cannot be loaded.

**Step 5: Verify with the current real leaderboard JSON**

Ensure six rows render from the current dataset.

**Step 6: Commit**

```bash
git add site/app.js site/index.html
git commit -m "feat: render leaderboard from live data"
```

### Task 4: Add publish-ready copy and deployment notes

**Files:**
- Modify: `D:/openclaw-agent-security/site/index.html`
- Create: `D:/openclaw-agent-security/site/README.md`

**Step 1: Refine copy**

Make sure the page clearly explains:

- what OpenClaw measures
- what the preview status means
- where methodology and raw artifacts live

**Step 2: Add deployment notes**

Document how to host `site/` on a static platform and what relative files must be published alongside it.

**Step 3: Verify final output manually**

Check that links and content remain coherent.

**Step 4: Commit**

```bash
git add site/index.html site/README.md
git commit -m "docs: prepare static leaderboard site for publish"
```
