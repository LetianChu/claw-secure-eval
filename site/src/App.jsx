import { useEffect, useState } from 'react';
import LeaderboardTable from './components/LeaderboardTable.jsx';
import ModelDetailModal from './components/ModelDetailModal.jsx';
import { getCopy, getInitialLanguage, LANGUAGE_STORAGE_KEY } from './lib/i18n.js';
import { loadLeaderboard } from './lib/leaderboard.js';
import './styles/theme.css';
import './styles/app.css';

const THEME_STORAGE_KEY = 'openclaw-leaderboard-theme';

function formatCount(value, label, language) {
  return language === 'zh' ? `${value}${label}` : `${value} ${label}`;
}

function DataStatePanel({ eyebrow, title, description, tone = 'loading' }) {
  return (
    <section className={`panel panel-state panel-state-${tone}`}>
      <p className="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
      <p>{description}</p>
    </section>
  );
}

function getInitialTheme() {
  if (typeof window === 'undefined') {
    return 'dark';
  }

  if (
    !window.localStorage ||
    typeof window.localStorage.getItem !== 'function'
  ) {
    return 'dark';
  }

  return window.localStorage.getItem(THEME_STORAGE_KEY) ?? 'dark';
}

export default function App() {
  const [state, setState] = useState({ status: 'loading', data: null, error: null });
  const [theme, setTheme] = useState(getInitialTheme);
  const [language, setLanguage] = useState(getInitialLanguage);
  const [selectedModel, setSelectedModel] = useState(null);
  const copy = getCopy(language);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    if (window.localStorage && typeof window.localStorage.setItem === 'function') {
      window.localStorage.setItem(THEME_STORAGE_KEY, theme);
    }
  }, [theme]);

  useEffect(() => {
    if (window.localStorage && typeof window.localStorage.setItem === 'function') {
      window.localStorage.setItem(LANGUAGE_STORAGE_KEY, language);
    }
  }, [language]);

  useEffect(() => {
    let cancelled = false;

    async function hydrateLeaderboard() {
      try {
        const data = await loadLeaderboard();
        if (!cancelled) setState({ status: 'ready', data, error: null });
      } catch (error) {
        if (!cancelled) {
          setState({
            status: 'error',
            data: null,
            error: error instanceof Error ? error.message : 'Unable to load leaderboard data.',
          });
        }
      }
    }

    hydrateLeaderboard();
    return () => {
      cancelled = true;
    };
  }, []);

  if (state.status === 'loading') {
    return (
      <div className="page-shell compact-shell">
        <main className="app-frame">
          <DataStatePanel
            eyebrow={copy.leaderboardData}
            title={copy.loadingTitle}
            description={copy.loadingDescription}
          />
        </main>
      </div>
    );
  }

  if (state.status === 'error' || !state.data?.summary) {
    return (
      <div className="page-shell compact-shell">
        <main className="app-frame">
          <DataStatePanel
            eyebrow={copy.leaderboardData}
            tone="error"
            title={copy.loadErrorTitle}
            description={state.error ?? copy.loadErrorDescription}
          />
        </main>
      </div>
    );
  }

  const { rows, summary } = state.data;
  const chips = [
    `${copy.updatedLabel} ${summary.lastUpdated}`,
    formatCount(summary.modelCount, copy.modelsLabel, language),
    formatCount(summary.taskCount, copy.tasksLabel, language),
    formatCount(summary.runCount, copy.runsLabel, language),
  ];

  return (
    <div className="page-shell compact-shell">
      <main className="app-frame">
        <header className="site-header">
          <div className="brand-row">
            <div className="brand-block">
              <span className="brand-wordmark">OpenClaw Security</span>
              <span className="brand-sub">{copy.navLeaderboard}</span>
            </div>
            <nav className="primary-nav" aria-label={copy.navAriaLabel}>
              <a href="#leaderboard">{copy.navLeaderboard}</a>
              <a href="#benchmark">{copy.navBenchmark}</a>
            </nav>

            <button
              className="theme-toggle"
              type="button"
              onClick={() => setLanguage((current) => (current === 'en' ? 'zh' : 'en'))}
              aria-label={copy.switchLanguage}
            >
              {copy.languageToggleLabel}
            </button>

            <button
              className="theme-toggle"
              type="button"
              onClick={() => setTheme((current) => (current === 'light' ? 'dark' : 'light'))}
              aria-label={copy.themeToggle}
            >
              {theme === 'light' ? copy.themeDark : copy.themeLight}
            </button>
          </div>

          <div className="title-row">
            <div>
              <p className="eyebrow">{copy.titleEyebrow}</p>
              <h1>{copy.appTitle}</h1>
            </div>
            <p className="title-meta">{copy.updatedLabel} {summary.lastUpdated}</p>
          </div>

          <div className="category-row" aria-label={copy.categoryTabsLabel}>
            <span className="category-pill is-active">{copy.categoryPreview}</span>
            <span className="category-pill">{copy.categoryCurrent}</span>
            <span className="category-pill">{copy.categoryRuntime}</span>
          </div>

          <div className="stats-row">
            {chips.map((chip) => (
              <span className="stat-pill" key={chip}>
                {chip}
              </span>
            ))}
          </div>
        </header>

        <section className="leaderboard-shell panel" id="leaderboard">
          <div className="leaderboard-shell-head">
            <div>
              <p className="eyebrow">{copy.rankingsEyebrow}</p>
              <h2>{copy.rankingsTitle}</h2>
            </div>
            <div className="leaderboard-actions">
              <span>{formatCount(summary.modelCount, copy.modelsLabel, language)}</span>
            </div>
          </div>

          <LeaderboardTable
            rows={rows}
            lastUpdated={summary.lastUpdated}
            modelCount={summary.modelCount}
            language={language}
            onRowClick={(row) => setSelectedModel(row)}
          />
        </section>

        {selectedModel && (
          <ModelDetailModal
            entry={selectedModel}
            onClose={() => setSelectedModel(null)}
            language={language}
          />
        )}

        <section className="subgrid" id="benchmark">
          <section className="panel info-panel">
            <p className="eyebrow">{copy.benchmarkEyebrow}</p>
            <h3>{copy.benchmarkTitle}</h3>
            <ul className="info-list">
              <li>{copy.benchmarkVersionLabel}: {summary.benchmarkVersion}</li>
              <li>{copy.profileLabel}: {summary.profileId}</li>
              <li>
                {copy.coverageLabel}: {formatCount(summary.taskCount, copy.tasksLabel, language)},{' '}
                {formatCount(summary.runCount, copy.runsLabel, language)}
              </li>
              <li>{copy.currentLeaderLabel}: {summary.leader.modelId}</li>
            </ul>
          </section>

          <section className="panel info-panel">
            <p className="eyebrow">{copy.notesEyebrow}</p>
            <h3>{copy.notesTitle}</h3>
            <p>{copy.notesDescription}</p>
            <p className="notes-attribution">
              Author: <a
                className="notes-attribution-link"
                href="https://leonchu.com"
                target="_blank"
                rel="noopener noreferrer"
              >
                leonchu.com
              </a>
            </p>
          </section>
        </section>
      </main>
    </div>
  );
}
