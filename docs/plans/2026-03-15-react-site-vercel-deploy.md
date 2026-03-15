# React Site Vercel Deploy Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the current React leaderboard site deploy cleanly from the existing repository on Vercel without splitting into a separate frontend repo.

**Architecture:** Keep the site under `site/`, use Vercel’s project root-directory support, and document the exact build/output settings. Add only minimal config needed for smooth static deployment.

**Tech Stack:** Vercel, Vite, React, static build output

---

### Task 1: Add minimal Vercel config and docs

**Files:**
- Create: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/vercel.json`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/README.md`

**Step 1: Add `vercel.json` only if needed**

Keep it minimal. Prefer settings that align with a static Vite app.

**Step 2: Update `site/README.md`**

Document:

- Vercel project should point to the current repo
- Root Directory: `site`
- Build Command: `npm run build`
- Output Directory: `dist`

**Step 3: Verify build still works**

Run: `npm run build`

Expected: PASS.

### Task 2: Verify deploy readiness in local docs

**Files:**
- Modify as needed: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/README.md`

**Step 1: Make deployment guidance explicit**

Add the exact click-path or settings a user needs in Vercel.

**Step 2: Note current data behavior**

Clarify that leaderboard data is bundled at build time from the repo artifact.

**Step 3: Re-run verification**

Run: `npm test -- --run` and `npm run build`

Expected: PASS.
