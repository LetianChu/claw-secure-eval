import assert from 'node:assert/strict';
import { createServer } from 'vite';
import { renderToStaticMarkup } from 'react-dom/server';

const server = await createServer({
  appType: 'custom',
  server: { middlewareMode: true },
});

try {
  const { default: App } = await server.ssrLoadModule('/src/App.jsx');
  const markup = renderToStaticMarkup(App());

  assert.match(
    markup,
    /<a[^>]+href="docs\/plans\/2026-03-10-openclaw-security-benchmark-v1-36-design\.md"/,
    'Expected benchmark design artifact path to render as a link.',
  );

  assert.match(
    markup,
    /<a[^>]+href="evaluator\/results\/model-results\/preview-v1\/moonshot__kimi-k2\.5-full-current\.json"/,
    'Expected model aggregate artifact path to render as a link.',
  );

  console.log('Artifact link regression test passed.');
} finally {
  await server.close();
}
