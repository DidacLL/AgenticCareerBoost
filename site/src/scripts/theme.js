const STORAGE_KEY = "didac-site-theme";
const root = document.documentElement;

function applyTheme(theme) {
  root.dataset.theme = theme;

  document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    button.textContent = theme === "dark" ? "light mode" : "dark mode";
    button.setAttribute("aria-pressed", String(theme === "dark"));
  });
}

function toggleTheme() {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";

  localStorage.setItem(STORAGE_KEY, nextTheme);
  applyTheme(nextTheme);
}

const storedTheme = localStorage.getItem(STORAGE_KEY);
applyTheme(storedTheme === "dark" ? "dark" : "light");

document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
  button.addEventListener("click", toggleTheme);
});
