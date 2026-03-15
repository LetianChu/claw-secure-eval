export default function SectionHeader({ eyebrow, title, description }) {
  return (
    <header className="section-header">
      <p className="eyebrow">{eyebrow}</p>
      <div>
        <h2>{title}</h2>
        <p>{description}</p>
      </div>
    </header>
  );
}
