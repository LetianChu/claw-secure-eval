# React Leaderboard Site Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a deployable `Vite + React` frontend under `site/` that presents the OpenClaw leaderboard in a launch-ready format and is structured for future expansion.

**Architecture:** Create a small React application with a clear split between data loading, page sections, and visual styling. The app stays static-host friendly by loading repository JSON artifacts client-side while keeping enough component structure to grow into a fuller product.

**Tech Stack:** Vite, React, TypeScript or JavaScript (choose one and keep it consistent), CSS, existing leaderboard JSON artifact

---

### Task 1: Scaffold the Vite + React app

**Files:**
- Create: `D:/openclaw-agent-security/site/package.json`
- Create: `D:/openclaw-agent-security/site/vite.config.*`
- Create: `D:/openclaw-agent-security/site/index.html`
- Create: `D:/openclaw-agent-security/site/src/main.*`
- Create: `D:/openclaw-agent-security/site/src/App.*`

**Step 1: Create the app scaffold**

Set up a minimal Vite + React application inside `site/`.

**Step 2: Add a placeholder app render**

Render a temporary shell so the app can boot.

**Step 3: Verify local startup/build path**

Run the project install and a build or dev-equivalent verification command.

**Step 4: Keep the scaffold minimal**

Do not add unnecessary libraries yet.

**Step 5: Commit**

```bash
git add site
git commit -m "feat: scaffold react leaderboard app"
```

### Task 2: Build the page layout and visual system

**Files:**
- Modify: `D:/openclaw-agent-security/site/src/App.*`
- Create: `D:/openclaw-agent-security/site/src/components/`
- Create: `D:/openclaw-agent-security/site/src/styles/`

**Step 1: Create page sections**

Implement:

- hero
- leaderboard section
- benchmark snapshot section
- methodology/artifacts section

**Step 2: Build the visual system**

Define CSS variables, spacing, typography, table styles, and responsive behavior.

**Step 3: Make the leaderboard table mobile-safe**

Use horizontal scrolling or other robust narrow-screen handling.

**Step 4: Verify visually**

Check the built page for desktop and mobile layout quality.

**Step 5: Commit**

```bash
git add site/src
git commit -m "feat: design react leaderboard homepage"
```

### Task 3: Wire the app to real leaderboard data

**Files:**
- Create or Modify: `D:/openclaw-agent-security/site/src/lib/`
- Modify: `D:/openclaw-agent-security/site/src/App.*`
- Modify: `D:/openclaw-agent-security/site/src/components/`

**Step 1: Implement data loading**

Load the current leaderboard JSON artifact from a path that works in the deployed static app.

**Step 2: Render leaderboard rows dynamically**

Use the real JSON fields to render model rows and page metadata.

**Step 3: Add loading and error states**

Handle missing or failed data fetches gracefully.

**Step 4: Verify with the current six-model dataset**

Confirm six rows render correctly from the live JSON.

**Step 5: Commit**

```bash
git add site/src
git commit -m "feat: render leaderboard from live artifact data"
```

### Task 4: Add publish-ready docs and deployment guidance

**Files:**
- Create: `D:/openclaw-agent-security/site/README.md`
- Modify: `D:/openclaw-agent-security/site/src/App.*`

**Step 1: Refine final copy**

Make the page text publish-ready and benchmark-accurate.

**Step 2: Document deployment**

Explain how to build and deploy the site and which artifact files it depends on.

**Step 3: Verify build output**

Run the production build.

**Step 4: Commit**

```bash
git add site
git commit -m "docs: prepare react leaderboard app for deployment"
```
