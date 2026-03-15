import { describe, expect, test } from 'vitest';
import { loadLeaderboard } from './leaderboard.js';

describe('loadLeaderboard', () => {
  test('loads and transforms the published leaderboard artifact', async () => {
    const data = await loadLeaderboard();

    expect(data.entries).toHaveLength(6);
    expect(data.rows).toHaveLength(6);
    expect(data.summary).toMatchObject({
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
    });

    expect(data.rows[0]).toMatchObject({
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
    });

    expect(data.rows[1]).toMatchObject({
      rank: '02',
      model: 'openai/gpt-5.2',
      status: 'Tied on score',
    });

    expect(data.rows[3]).toMatchObject({
      rank: '04',
      model: 'moonshot/kimi-k2.5',
      status: 'Published result',
      taskCompletionRate: '0.9333',
    });
  });
});
