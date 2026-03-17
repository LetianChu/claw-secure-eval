const modalCopy = {
  en: {
    close: 'Close',
    score: 'Score',
    passed: 'Passed',
    failed: 'Failed',
    taskDetails: 'Task Details',
    message: 'Message',
    trap: 'Hidden Trap',
    actual: 'Actual Behavior',
    verdict: {true: 'FAIL', false: 'PASS'},
    passCount: (p, f) => p + ' passed / ' + f + ' failed',
  },
  zh: {
    close: '关闭',
    score: '得分',
    passed: '通过',
    failed: '失败',
    taskDetails: '任务详情',
    message: '消息',
    trap: '隐藏陷阱',
    actual: '实际行为',
    verdict: {true: '失败', false: '通过'},
    passCount: (p, f) => p + ' 个通过 / ' + f + ' 个失败',
  },
};

export default function ModelDetailModal({ entry, onClose, language = 'en' }) {
  const copy = modalCopy[language] || modalCopy.en;
  const details = entry.task_details || [];
  const passed = details.filter(t => !t.boundary_failed).length;
  const failed = details.filter(t => t.boundary_failed).length;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <div>
            <h2>{entry.model}</h2>
            <span className="modal-meta">
              {copy.score}: {entry.securityScore} | {copy.passCount(passed, failed)}
            </span>
          </div>
          <button className="modal-close" onClick={onClose}>{copy.close}</button>
        </div>
        <div className="modal-body">
          {details.map(task => {
            const lang = language;
            const title = task.title?.[lang] || task.title?.en || task.task_id;
            const msg = task.msg?.[lang] || task.msg?.en || '';
            const trap = task.trap?.[lang] || task.trap?.en || '';
            const actual = task.actual?.[lang] || task.actual?.en || '';
            const isFail = task.boundary_failed;
            return (
              <div key={task.task_id} className={'task-card ' + (isFail ? 'task-fail' : 'task-pass')}>
                <div className="task-card-header">
                  <span className={'task-badge ' + (isFail ? 'badge-fail' : 'badge-pass')}>
                    {isFail ? '✗' : '✓'}
                  </span>
                  <strong>{task.task_id}</strong>
                  <span className="task-title">{title}</span>
                  <span className="task-score">{task.score}</span>
                </div>
                <div className="task-card-body">
                  <div className="task-row">
                    <span className="task-label">{copy.message}</span>
                    <span>{msg}</span>
                  </div>
                  <div className="task-row">
                    <span className="task-label">{copy.trap}</span>
                    <span>{trap}</span>
                  </div>
                  <div className="task-row">
                    <span className="task-label">{copy.actual}</span>
                    <span className="task-actual">{actual}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
