# React Site Bilingual Design

## Goal

Add a clean bilingual layer to the React leaderboard site with an `EN / 中文` toggle so the site stays publishable for an international audience without cluttering the page.

## Chosen Interaction

- top-right language toggle
- default language: English
- alternate language: Simplified Chinese

## Why This Approach

- preserves the compact leaderboard-first layout
- avoids doubling page height with side-by-side translation
- keeps the page aligned with public product-site expectations

## Scope

- navigation labels
- page title and metadata
- benchmark summary copy
- section headings and explanatory text
- table column labels and status labels where practical

## Data Strategy

- keep benchmark metrics and model ids unchanged
- translate UI strings only
- store strings in a small in-app dictionary rather than adding a heavy i18n framework

## UX Details

- expose an `EN / 中文` switch in the header
- persist the chosen language in local storage
- fall back to English if stored language is unavailable

## Success Criteria

- page can switch instantly between English and Chinese
- leaderboard structure remains compact
- no metric values or model identifiers are altered by translation
- tests and build remain green
