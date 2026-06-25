(() => {
  const panels = Array.from(document.querySelectorAll("[data-panel]"));
  const panelLinks = Array.from(document.querySelectorAll("[data-panel-link]"));
  const validPanels = new Set(panels.map((panel) => panel.dataset.panel));
  const params = new URLSearchParams(window.location.search);
  const requestedPanel = params.get("panel") || "intro";
  const activePanel = validPanels.has(requestedPanel) ? requestedPanel : "intro";
  const labels = {
    intro: ["INTRO", "Operator file"],
    work: ["WORK", "Projects and reports"],
    now: ["NOW", "Current status"],
    cv: ["CV", "Curriculum"],
    notes: ["NOTES", "Notes index"],
    hire: ["HIRE", "Role routes"],
    contact: ["CONTACT", "Direct links"],
  };

  document.documentElement.dataset.osReady = "true";

  function setPanel(panelName) {
    panels.forEach((panel) => {
      const isActive = panel.dataset.panel === panelName;
      panel.classList.toggle("is-active", isActive);
      panel.toggleAttribute("hidden", !isActive);
    });

    panelLinks.forEach((link) => {
      const isActive = link.dataset.panelLink === panelName;
      link.classList.toggle("is-active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });

    const [label, title] = labels[panelName] || labels.intro;
    document.querySelectorAll("[data-active-panel-label]").forEach((node) => {
      node.textContent = label;
    });
    document.querySelectorAll("[data-active-panel-title]").forEach((node) => {
      node.textContent = title;
    });
    document.querySelectorAll("[data-active-panel-meta]").forEach((node) => {
      node.textContent = title;
    });
  }

  function setTheme(theme) {
    const nextTheme = theme === "dark" ? "dark" : "light";
    document.documentElement.dataset.theme = nextTheme;
    localStorage.setItem("didac-os-theme", nextTheme);
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.textContent = nextTheme === "dark" ? "light mode" : "dark mode";
      button.setAttribute("aria-pressed", String(nextTheme === "dark"));
    });
  }

  setPanel(activePanel);
  setTheme(localStorage.getItem("didac-os-theme") || "light");

  document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const current = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
      setTheme(current === "dark" ? "light" : "dark");
    });
  });

  document.querySelectorAll("[data-holo-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const windowNode = button.closest("[data-holo-window]");
      if (!windowNode) return;
      const expanded = windowNode.classList.toggle("is-expanded");
      button.setAttribute("aria-expanded", String(expanded));
      button.textContent = expanded ? "minimize" : "maximize";
    });
  });
})();
