# React Homepage Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure the React leaderboard homepage so it feels closer to a compact leaderboard hub like llm-stats.com and less like a landing page.

**Architecture:** Keep the current React app and data flow, but replace the page skeleton with a denser header + category strip + leaderboard-first layout. Simplify secondary sections and shift the visual system toward a neutral, open-source documentation/product aesthetic.

**Tech Stack:** React, CSS, existing leaderboard JSON loader, Vitest

---

### Task 1: Replace the homepage skeleton with a leaderboard-first structure

**Files:**
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/App.jsx`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/styles/app.css`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/styles/theme.css`

**Step 1: Update tests for the new compact skeleton**

Run and adjust `site/src/App.test.jsx` so expectations match the denser layout instead of the older landing-page hero.

**Step 2: Rebuild the page structure**

Implement:

- sticky compact header
- compact title row
- lightweight category strip
- leaderboard table as the dominant first-screen block
- simplified lower benchmark notes

**Step 3: Tighten the visual system**

Reduce warm/editorial styling and shift toward neutral leaderboard/product UI.

**Step 4: Verify**

Run: `npm test -- --run` and `npm run build`

Expected: PASS.
