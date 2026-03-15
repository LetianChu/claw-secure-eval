export const LANGUAGE_STORAGE_KEY = 'openclaw-leaderboard-language';

export const translations = {
  en: {
    appTitle: 'OpenClaw Security Leaderboard',
    switchLanguage: 'Switch language',
    languageToggleLabel: 'EN / 中文',
    leaderboardData: 'Leaderboard data',
    loadingTitle: 'Loading leaderboard data.',
    loadingDescription:
      'Opening the published benchmark artifact and preparing the current rankings.',
    loadErrorTitle: 'Unable to load leaderboard data.',
    loadErrorDescription: 'The published artifact could not be read by the app.',
    navAriaLabel: 'Primary navigation',
    navLeaderboard: 'Leaderboards',
    navBenchmark: 'Benchmarks',
    themeToggle: 'Toggle theme',
    themeDark: 'Dark',
    themeLight: 'Light',
    titleEyebrow: 'AI Leaderboards',
    updatedLabel: 'Updated',
    categoryTabsLabel: 'Category tabs',
    categoryPreview: 'Preview V1',
    categoryCurrent: 'Current Real',
    categoryRuntime: 'OpenClaw Runtime',
    modelsLabel: 'models',
    tasksLabel: 'tasks',
    runsLabel: 'runs',
    rankingsEyebrow: 'Current Rankings',
    rankingsTitle: 'Top models ranked by security benchmark performance.',
    benchmarkEyebrow: 'Benchmark Snapshot',
    benchmarkTitle: 'Current baseline',
    benchmarkVersionLabel: 'Benchmark version',
    profileLabel: 'Profile',
    coverageLabel: 'Coverage',
    currentLeaderLabel: 'Current leader',
    notesEyebrow: 'Published Notes',
    notesTitle: 'What this page means',
    notesDescription:
      'Rankings describe security behavior inside a versioned OpenClaw benchmark. They are comparative benchmark results, not universal safety scores.',
  },
  zh: {
    appTitle: 'OpenClaw Security 安全排行榜',
    switchLanguage: '切换语言',
    languageToggleLabel: 'EN / 中文',
    leaderboardData: '排行榜数据',
    loadingTitle: '正在加载排行榜数据。',
    loadingDescription: '正在打开已发布的基准工件并准备当前排名。',
    loadErrorTitle: '无法加载排行榜数据。',
    loadErrorDescription: '应用无法读取已发布的工件。',
    navAriaLabel: '主导航',
    navLeaderboard: '排行榜',
    navBenchmark: '基准概览',
    themeToggle: '切换主题',
    themeDark: '深色',
    themeLight: '浅色',
    titleEyebrow: 'AI 排行榜',
    updatedLabel: '已更新',
    categoryTabsLabel: '分类标签',
    categoryPreview: '预览 V1',
    categoryCurrent: '当前实测',
    categoryRuntime: 'OpenClaw 运行时',
    modelsLabel: '个模型',
    tasksLabel: '个任务',
    runsLabel: '次运行',
    rankingsEyebrow: '当前排名',
    rankingsTitle: '按安全基准表现排序的领先模型。',
    benchmarkEyebrow: '基准快照',
    benchmarkTitle: '当前基线',
    benchmarkVersionLabel: '基准版本',
    profileLabel: '配置档',
    coverageLabel: '覆盖范围',
    currentLeaderLabel: '当前领先模型',
    notesEyebrow: '发布说明',
    notesTitle: '页面说明',
    notesDescription:
      '这些排名展示的是模型在版本化 OpenClaw 安全基准中的表现。它们是对比性的基准结果，并非通用安全评分。',
  },
};

export function getInitialLanguage() {
  if (typeof window === 'undefined') {
    return 'en';
  }

  if (
    !window.localStorage ||
    typeof window.localStorage.getItem !== 'function'
  ) {
    return 'en';
  }

  const storedLanguage = window.localStorage.getItem(LANGUAGE_STORAGE_KEY);
  return storedLanguage === 'zh' ? 'zh' : 'en';
}

export function getCopy(language) {
  return translations[language] ?? translations.en;
}
