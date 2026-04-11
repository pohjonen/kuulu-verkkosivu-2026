// Minimal progressive enhancement only.
(function () {
  const root = document.currentScript && document.currentScript.closest('.kuulu-hero-cinematic-v2');
  if (!root) return;
  root.dataset.heroReady = 'true';
})();
