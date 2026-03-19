const modalCopy = {
  en: {
    close: 'Close',
    score: 'Score',
    trap: 'Hidden Trap',
    sent: 'Messages Sent to OpenClaw',
    behavior: 'What OpenClaw Did',
    operator: 'Operator',
    external: 'External Content (injected)',
    dangerTag: 'UNSAFE',
    passCount: (p, f) => p + ' passed / ' + f + ' failed',
  },
  zh: {
    close: '关闭',
    score: '得分',
    trap: '隐藏陷阱',
    sent: '发送给 OpenClaw 的指令',
    behavior: 'OpenClaw 实际做了什么',
    operator: '操作员',
    external: '外部内容（注入）',
    dangerTag: '不安全',
    passCount: (p, f) => p + ' 个通过 / ' + f + ' 个失败',
  },
};

function SenderLabel({ sender, copy }) {
  const isExternal = sender === 'external_content';
  return (
    <span className={'sender-label ' + (isExternal ? 'sender-external' : 'sender-operator')}>
      {isExternal ? copy.external : copy.operator}
    </span>
  );
}

function StepLine({ step, copy }) {
  return (
    <div className={'step-line ' + (step.danger ? 'step-danger' : '')}>
      {step.danger && <span className="danger-tag">{copy.dangerTag}</span>}
      <span className="step-text">{step.action}</span>
      {step.response && (
        <pre className="step-response">{step.response}</pre>
      )}
    </div>
  );
}

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
            const trap = task.trap?.[lang] || task.trap?.en || '';
            const messages = task.messages || [];
            const steps = task.steps || [];
            const isFail = task.boundary_failed;
            return (
              <div key={task.task_id} className={'task-card ' + (isFail ? 'task-fail' : 'task-pass')}>
                <div className="task-card-header">
                  <span className={'task-badge ' + (isFail ? 'badge-fail' : 'badge-pass')}>
                    {isFail ? '\u2717' : '\u2713'}
                  </span>
                  <strong>{task.task_id}</strong>
                  <span className="task-title">{title}</span>
                  <span className="task-score">{task.score}</span>
                </div>
                <div className="task-card-body">
                  <div className="task-section">
                    <span className="task-label">{copy.trap}</span>
                    <span className="trap-text">{trap}</span>
                  </div>
                  <div className="task-section">
                    <span className="task-label">{copy.sent}</span>
                    <div className="message-list">
                      {messages.map((m, i) => (
                        <div key={i} className="message-item">
                          <SenderLabel sender={m.sender} copy={copy} />
                          <span className="message-text">{m.text}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="task-section">
                    <span className="task-label">{copy.behavior}</span>
                    <div className="steps-list">
                      {steps.map((s, i) => (
                        <StepLine key={i} step={s} copy={copy} />
                      ))}
                    </div>
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
