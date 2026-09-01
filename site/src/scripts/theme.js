const root = document.documentElement;
const storageKey = root.dataset.themeStorageKey;

function label(button, theme) {
  const nextLabel = theme === "dark" ? button.dataset.labelLight : button.dataset.labelDark;
  if (nextLabel) button.textContent = nextLabel;
  button.setAttribute("aria-pressed", String(theme === "dark"));
}

function applyTheme(theme, persist = true) {
  root.dataset.theme = theme;
  if (persist && storageKey) localStorage.setItem(storageKey, theme);
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => label(button, theme));
}

document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
  label(button, root.dataset.theme === "dark" ? "dark" : "light");
  button.addEventListener("click", () => {
    applyTheme(root.dataset.theme === "dark" ? "light" : "dark");
  });
});