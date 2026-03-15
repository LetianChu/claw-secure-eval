# React Site Bilingual Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an `EN / 中文` language switch to the React leaderboard site while keeping the page compact and launch-ready.

**Architecture:** Use a lightweight in-app translation dictionary plus a small language state hook, rather than introducing a full i18n framework. Persist the selected language in local storage and apply translated UI strings throughout the current page structure.

**Tech Stack:** React, existing app state, local storage, Vitest

---

### Task 1: Add language state and translation dictionary

**Files:**
- Create: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/lib/i18n.js`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/App.jsx`
- Test: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/App.test.jsx`

**Step 1: Write the failing test**

Add a test that expects the page to render in English by default and switch to Chinese when the toggle is used.

**Step 2: Run test to verify it fails**

Run: `npm test -- --run`

Expected: FAIL because no language switch exists yet.

**Step 3: Implement minimal language state**

Add:

- translation dictionary
- current language state
- local storage persistence

**Step 4: Run tests to verify green**

Run: `npm test -- --run`

Expected: PASS.

### Task 2: Apply translations to page chrome and section copy

**Files:**
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/App.jsx`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/components/SectionHeader.jsx`

**Step 1: Translate header UI**

Apply translations to:

- navigation labels
- title/meta labels
- category chips
- section titles and explanatory text

**Step 2: Keep metrics unmodified**

Do not translate model ids or metric values.

**Step 3: Verify manually through tests/build**

Run: `npm test -- --run` and `npm run build`

Expected: PASS.

### Task 3: Translate leaderboard table labels and status copy

**Files:**
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/components/LeaderboardTable.jsx`
- Modify: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/App.test.jsx`

**Step 1: Translate table headers and status labels**

Translate only UI labels, not data values.

**Step 2: Verify both languages render correctly**

Run: `npm test -- --run`

Expected: PASS.

### Task 4: Final verification and polish

**Files:**
- Modify as needed: `D:/openclaw-agent-security/.worktrees/react-leaderboard-site/site/src/styles/app.css`

**Step 1: Make sure the language toggle fits the compact header**

Adjust styling if needed.

**Step 2: Run final verification**

Run: `npm test -- --run` and `npm run build`

Expected: PASS.
