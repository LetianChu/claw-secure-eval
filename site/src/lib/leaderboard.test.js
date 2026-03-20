import { describe, expect, test } from 'vitest';
import { loadLeaderboard } from './leaderboard.js';

describe('loadLeaderboard', () => {
  test('loads and transforms the published leaderboard artifact', async () => {
    const data = await loadLeaderboard();

    expect(data.entries).toHaveLength(15);
    expect(data.rows).toHaveLength(15);
    expect(data.summary).toMatchObject({
      benchmarkVersion: 'preview-v1-current-real',
      profileId: 'openclaw-preview-v1',
      modelCount: 15,
      taskCount: 15,
      runCount: 225,
      leader: {
        modelId: 'anthropic/claude-opus-4-6',
        securityScore: '100.00',
        boundaryFailureRate: '0.0000',
        approvalPreservedRate: '1.0000',
        persistenceViolationRate: '0.0000',
        taskCompletionRate: '0.8667',
        tasksEvaluated: 15,
        runsEvaluated: 15,
      },
    });

    expect(data.rows[0]).toMatchObject({
      rank: '01',
      model: 'anthropic/claude-opus-4-6',
      securityScore: '100.00',
      status: 'Current leader',
      metadata: '15 tasks / 15 runs',
    });

    expect(data.rows[0].task_details).toBeDefined();
    expect(data.rows[0].task_details.length).toBe(15);

    const firstTask = data.rows[0].task_details[0];
    expect(firstTask).toMatchObject({
      task_id: 'AE-001',
      score: expect.any(Number),
      boundary_failed: expect.any(Boolean),
    });
    expect(firstTask.title).toBeDefined();
    expect(firstTask.messages).toBeDefined();
    expect(firstTask.trap).toBeDefined();
    expect(firstTask.steps).toBeDefined();
  });
});
