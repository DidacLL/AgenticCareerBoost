function currentTheme(root = document.documentElement) {
  return root.dataset.theme === "dark" ? "dark" : "light";
}

function label(button, theme) {
  const nextLabel = theme === "dark" ? button.dataset.labelLight : button.dataset.labelDark;
  if (nextLabel) button.textContent = nextLabel;
  button.setAttribute("aria-pressed", String(theme === "dark"));
}

function applyTheme(theme, persist = true) {
  const root = document.documentElement;
  const storageKey = root.dataset.themeStorageKey;
  root.dataset.theme = theme;
  if (persist && storageKey) localStorage.setItem(storageKey, theme);
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => label(button, theme));
}

function wireThemeToggles() {
  const theme = currentTheme();
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    label(button, theme);
    if (button.dataset.themeWired === "true") return;
    button.dataset.themeWired = "true";
    button.addEventListener("click", () => {
      applyTheme(currentTheme() === "dark" ? "light" : "dark");
    });
  });
}

function syncThemeToIncomingDocument(event) {
  const root = document.documentElement;
  const storageKey = root.dataset.themeStorageKey;
  const stored = storageKey ? localStorage.getItem(storageKey) : null;
  event.newDocument.documentElement.dataset.theme = stored === "dark" || stored === "light" ? stored : currentTheme(root);
}

wireThemeToggles();
if (!window.__acbThemeLifecycleWired) {
  window.__acbThemeLifecycleWired = true;
  document.addEventListener("astro:page-load", wireThemeToggles);
  document.addEventListener("astro:before-swap", syncThemeToIncomingDocument);
}
