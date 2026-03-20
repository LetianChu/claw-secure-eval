const tableCopy = {
  en: {
    captionTitle: 'Preview leaderboard',
    captionSummary: (modelCount, lastUpdated) =>
      `${modelCount} models loaded from the current artifact. Updated ${lastUpdated}.`,
    regionLabel: 'ClawSafeBench leaderboard',
    columns: {
      rank: 'Rank',
      model: 'Model',
      securityScore: 'Security score',
      boundaryFailureRate: 'Boundary failure',
      approvalPreservedRate: 'Approval preserved',
      persistenceViolationRate: 'Persistence violation',
      taskCompletionRate: 'Task completion',
      status: 'Result status',
    },
    statusLabels: {
      'Current leader': 'Current leader',
      'Published result': 'Published result',
      'Tied on score': 'Tied on score',
    },
    updatedPrefix: 'Updated',
  },
  zh: {
    captionTitle: '预览排行榜',
    captionSummary: (modelCount, lastUpdated) =>
      `当前工件已载入 ${modelCount} 个模型。已更新 ${lastUpdated}。`,
    regionLabel: 'ClawSafeBench 排行榜',
    columns: {
      rank: '排名',
      model: '模型',
      securityScore: '安全得分',
      boundaryFailureRate: '越界失败率',
      approvalPreservedRate: '审批保持率',
      persistenceViolationRate: '持久化违规率',
      taskCompletionRate: '任务完成率',
      status: '结果状态',
    },
    statusLabels: {
      'Current leader': '当前领先',
      'Published result': '已发布结果',
      'Tied on score': '分数并列',
    },
    updatedPrefix: '已更新',
  },
};

function getColumns(copy) {
  return [
    { key: 'rank', label: copy.columns.rank },
    { key: 'model', label: copy.columns.model },
    { key: 'securityScore', label: copy.columns.securityScore },
    { key: 'boundaryFailureRate', label: copy.columns.boundaryFailureRate },
    { key: 'approvalPreservedRate', label: copy.columns.approvalPreservedRate },
    { key: 'persistenceViolationRate', label: copy.columns.persistenceViolationRate },
    { key: 'taskCompletionRate', label: copy.columns.taskCompletionRate },
    { key: 'status', label: copy.columns.status },
  ];
}

function getTranslatedMetadata(metadata, language) {
  if (language !== 'zh') {
    return metadata;
  }

  const match = metadata.match(/^(\d+) tasks \/ (\d+) runs$/);
  if (!match) {
    return metadata;
  }

  const [, tasks, runs] = match;
  return `${tasks}个任务 / ${runs}次运行`;
}

function getTranslatedMetadataDetail(metadataDetail, copy, language) {
  if (language !== 'zh') {
    return metadataDetail;
  }

  if (metadataDetail.startsWith('Updated ')) {
    return `${copy.updatedPrefix} ${metadataDetail.slice('Updated '.length)}`;
  }

  return metadataDetail;
}

export default function LeaderboardTable({ rows, lastUpdated, modelCount, language = 'en', onRowClick }) {
  const copy = tableCopy[language] ?? tableCopy.en;
  const columns = getColumns(copy);

  return (
    <div className="leaderboard-table-shell">
      <div className="table-caption-row">
        <p>{copy.captionTitle}</p>
        <span>
          {copy.captionSummary(modelCount, lastUpdated)}
        </span>
      </div>

      <div className="leaderboard-table-wrap" role="region" aria-label={copy.regionLabel}>
        <table className="leaderboard-table">
          <thead>
            <tr>
              {columns.map((column) => (
                <th key={column.key} scope="col">
                  {column.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.key} onClick={() => onRowClick && onRowClick(row)} style={{cursor: onRowClick ? 'pointer' : 'default'}}>
                {columns.map((column) => (
                  <td key={column.key} data-label={column.label}>
                    {column.key === 'status' ? (
                      <div className="status-stack">
                        <span className="status-pill">{copy.statusLabels[row[column.key]] ?? row[column.key]}</span>
                        <small>{getTranslatedMetadata(row.metadata, language)}</small>
                        <small>{getTranslatedMetadataDetail(row.metadataDetail, copy, language)}</small>
                      </div>
                    ) : (
                      row[column.key]
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
