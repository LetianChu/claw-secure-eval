const DECIMAL_FORMATS = {
  security_score: 2,
  boundary_failure_rate: 4,
  approval_preserved_rate: 4,
  persistence_violation_rate: 4,
  task_completion_rate: 4,
};

function formatDecimal(value, digits) {
  return Number(value).toFixed(digits);
}

function formatRank(rank) {
  return String(rank).padStart(2, '0');
}

function formatTimestamp(timestamp) {
  return `${new Intl.DateTimeFormat('en-US', {
    dateStyle: 'medium',
    timeStyle: 'short',
    timeZone: 'UTC',
  }).format(new Date(timestamp))} UTC`;
}

function getRowMeta(entry) {
  return `${entry.tasks_evaluated} tasks / ${entry.runs_evaluated} runs`;
}

function getRowStatus(entry, topScore) {
  if (entry.rank === 1) {
    return 'Current leader';
  }

  if (entry.security_score === topScore) {
    return 'Tied on score';
  }

  return 'Published result';
}

export function buildLeaderboardModel(entries) {
  if (!Array.isArray(entries) || entries.length === 0) {
    return {
      entries: [],
      rows: [],
      summary: null,
    };
  }

  const sortedEntries = [...entries].sort((left, right) => left.rank - right.rank);
  const leader = sortedEntries[0];
  const uniqueTaskIds = new Set(sortedEntries.flatMap((entry) => entry.task_ids));
  const latestUpdate = sortedEntries.reduce((latest, entry) => {
    if (!latest || new Date(entry.last_updated) > new Date(latest)) {
      return entry.last_updated;
    }

    return latest;
  }, null);
  const topScore = Math.max(...sortedEntries.map((entry) => entry.security_score));

  return {
    entries: sortedEntries,
    rows: sortedEntries.map((entry) => ({
      key: entry.model_id,
      rank: formatRank(entry.rank),
      model: entry.model_id,
      securityScore: formatDecimal(entry.security_score, DECIMAL_FORMATS.security_score),
      boundaryFailureRate: formatDecimal(
        entry.boundary_failure_rate,
        DECIMAL_FORMATS.boundary_failure_rate,
      ),
      approvalPreservedRate: formatDecimal(
        entry.approval_preserved_rate,
        DECIMAL_FORMATS.approval_preserved_rate,
      ),
      persistenceViolationRate: formatDecimal(
        entry.persistence_violation_rate,
        DECIMAL_FORMATS.persistence_violation_rate,
      ),
      taskCompletionRate: formatDecimal(
        entry.task_completion_rate,
        DECIMAL_FORMATS.task_completion_rate,
      ),
      status: getRowStatus(entry, topScore),
      metadata: getRowMeta(entry),
      metadataDetail: `Updated ${formatTimestamp(entry.last_updated)}`,
      task_details: entry.task_details || [],
    })),
    summary: {
      benchmarkVersion: leader.benchmark_version,
      profileId: leader.profile_id,
      modelCount: sortedEntries.length,
      taskCount: uniqueTaskIds.size,
      runCount: sortedEntries.reduce((total, entry) => total + entry.runs_evaluated, 0),
      lastUpdated: formatTimestamp(latestUpdate),
      leader: {
        modelId: leader.model_id,
        securityScore: formatDecimal(leader.security_score, DECIMAL_FORMATS.security_score),
        boundaryFailureRate: formatDecimal(
          leader.boundary_failure_rate,
          DECIMAL_FORMATS.boundary_failure_rate,
        ),
        approvalPreservedRate: formatDecimal(
          leader.approval_preserved_rate,
          DECIMAL_FORMATS.approval_preserved_rate,
        ),
        persistenceViolationRate: formatDecimal(
          leader.persistence_violation_rate,
          DECIMAL_FORMATS.persistence_violation_rate,
        ),
        taskCompletionRate: formatDecimal(
          leader.task_completion_rate,
          DECIMAL_FORMATS.task_completion_rate,
        ),
        tasksEvaluated: leader.tasks_evaluated,
        runsEvaluated: leader.runs_evaluated,
      },
    },
  };
}

export async function loadLeaderboard() {
  try {
    const leaderboardModule = await import('../../../leaderboard/output/preview-leaderboard.json');

    return buildLeaderboardModel(leaderboardModule.default ?? leaderboardModule);
  } catch (error) {
    throw new Error('Unable to load leaderboard data.', { cause: error });
  }
}
