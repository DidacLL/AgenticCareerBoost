const key = "didac-site-theme";
const root = document.documentElement;
const apply = (theme) => {
  root.dataset.theme = theme;
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    button.textContent = theme === "dark" ? "light mode" : "dark mode";
    button.setAttribute("aria-pressed", String(theme === "dark"));
  });
};
apply(localStorage.getItem(key) === "dark" ? "dark" : "light");
document.querySelectorAll("[data-theme-toggle]").forEach((button) => button.addEventListener("click", () => {
  const next = root.dataset.theme === "dark" ? "light" : "dark";
  localStorage.setItem(key, next);
  apply(next);
}));
