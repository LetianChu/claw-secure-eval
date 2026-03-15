// @vitest-environment jsdom
import '@testing-library/jest-dom/vitest';
import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, test, vi } from 'vitest';

vi.mock('./lib/leaderboard.js', () => ({
  loadLeaderboard: vi.fn(),
}));

import App from './App.jsx';
import { loadLeaderboard } from './lib/leaderboard.js';

const sampleData = {
  rows: [
    {
      key: 'openai/gpt-5.1-codex',
      rank: '01',
      model: 'openai/gpt-5.1-codex',
      securityScore: '96.67',
      boundaryFailureRate: '0.0667',
      approvalPreservedRate: '1.0000',
      persistenceViolationRate: '0.0000',
      taskCompletionRate: '0.8667',
      status: 'Current leader',
      metadata: '15 tasks / 15 runs',
      metadataDetail: 'Updated Mar 15, 2026, 12:23 PM UTC',
    },
    {
      key: 'moonshot/kimi-k2.5',
      rank: '04',
      model: 'moonshot/kimi-k2.5',
      securityScore: '86.67',
      boundaryFailureRate: '0.2667',
      approvalPreservedRate: '1.0000',
      persistenceViolationRate: '0.0000',
      taskCompletionRate: '0.9333',
      status: 'Published result',
      metadata: '15 tasks / 15 runs',
      metadataDetail: 'Updated Mar 15, 2026, 12:23 PM UTC',
    },
  ],
  summary: {
    benchmarkVersion: 'preview-v1-current-real',
    profileId: 'openclaw-preview-v1',
    modelCount: 6,
    taskCount: 15,
    runCount: 90,
    lastUpdated: 'Mar 15, 2026, 12:23 PM UTC',
    leader: {
      modelId: 'openai/gpt-5.1-codex',
      securityScore: '96.67',
      boundaryFailureRate: '0.0667',
      approvalPreservedRate: '1.0000',
      persistenceViolationRate: '0.0000',
      taskCompletionRate: '0.8667',
      tasksEvaluated: 15,
      runsEvaluated: 15,
    },
  },
};

const dynamicSampleData = {
  ...sampleData,
  summary: {
    ...sampleData.summary,
    modelCount: 3,
    taskCount: 12,
    runCount: 36,
  },
};

describe('App', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    cleanup();
  });

  test('shows a loading state before leaderboard data resolves', () => {
    vi.mocked(loadLeaderboard).mockReturnValue(new Promise(() => {}));

    render(<App />);

    expect(screen.getByText(/loading leaderboard data/i)).toBeInTheDocument();
  });

  test('renders leaderboard rows and metadata from loaded data', async () => {
    vi.mocked(loadLeaderboard).mockResolvedValue(sampleData);

    render(<App />);

    expect(await screen.findByText('openai/gpt-5.1-codex')).toBeInTheDocument();
    expect(screen.getByText('moonshot/kimi-k2.5')).toBeInTheDocument();
    expect(document.documentElement.dataset.theme).toBe('dark');
    expect(screen.getByText('Preview V1')).toBeInTheDocument();
    expect(screen.getByText('Current Real')).toBeInTheDocument();
    expect(screen.getAllByText(/updated mar 15, 2026, 12:23 pm utc/i).length).toBeGreaterThan(0);
    expect(screen.getAllByText('6 models').length).toBeGreaterThan(0);
    expect(screen.getAllByText('15 tasks / 15 runs')).toHaveLength(2);
    expect(screen.getAllByText(/updated mar 15, 2026, 12:23 pm utc/i).length).toBeGreaterThan(0);
  });

  test('derives hero counts from loaded data and avoids broken public artifact links', async () => {
    vi.mocked(loadLeaderboard).mockResolvedValue(dynamicSampleData);

    render(<App />);

    expect(await screen.findByText(/openclaw security leaderboard/i)).toBeInTheDocument();
    expect(screen.getAllByText('3 models').length).toBeGreaterThan(0);
    expect(screen.getAllByText('12 tasks').length).toBeGreaterThan(0);
    expect(
      screen.queryByRole('link', { name: /leaderboard\/output\/preview-leaderboard\.json/i }),
    ).not.toBeInTheDocument();
    expect(
      screen.queryByRole('link', { name: /docs\/plans\/2026-03-10-openclaw-security-benchmark-v1-36-design\.md/i }),
    ).not.toBeInTheDocument();
  });

  test('shows an error state when data loading fails', async () => {
    vi.mocked(loadLeaderboard).mockRejectedValue(new Error('Unable to load leaderboard data.'));

    render(<App />);

    expect(
      await screen.findByRole('heading', { name: /unable to load leaderboard data/i }),
    ).toBeInTheDocument();
  });

  test('defaults to English and switches to Chinese after toggle', async () => {
    vi.mocked(loadLeaderboard).mockResolvedValue(sampleData);

    render(<App />);

    expect(await screen.findByRole('heading', { name: 'OpenClaw Security Leaderboard' })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: 'Leaderboards' })).toBeInTheDocument();
    expect(screen.getByText('Current Rankings')).toBeInTheDocument();
    expect(screen.getByText('What this page means')).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: /switch language/i }));

    expect(await screen.findByRole('heading', { name: 'OpenClaw Security 安全排行榜' })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: '排行榜' })).toBeInTheDocument();
    expect(screen.getByText('当前排名')).toBeInTheDocument();
    expect(screen.getByText('页面说明')).toBeInTheDocument();
    expect(screen.getByRole('columnheader', { name: '排名' })).toBeInTheDocument();
    expect(screen.getByRole('columnheader', { name: '结果状态' })).toBeInTheDocument();
    expect(screen.getByText('当前领先')).toBeInTheDocument();
    expect(screen.getByText('已发布结果')).toBeInTheDocument();
  });
});
