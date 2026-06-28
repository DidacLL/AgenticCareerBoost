(function () {
  const allowed = new Set(["ml", "agentic", "backend", "print"]);

  function appliesTo(node, view) {
    const views = (node.dataset.views || "").split(/\s+/).filter(Boolean);
    return views.length === 0 || views.includes(view) || view === "print";
  }

  function currentView() {
    const params = new URLSearchParams(window.location.search);
    const requested = params.get("view") || "ml";
    return allowed.has(requested) ? requested : "ml";
  }

  function initCvView() {
    const view = currentView();
    document.documentElement.dataset.cvView = view;

    document.querySelectorAll("[data-views]").forEach((node) => {
      const visible = appliesTo(node, view);
      node.hidden = !visible;
      node.classList.toggle("is-visible", visible);
    });

    document.querySelectorAll("button[data-cv-view]").forEach((button) => {
      const target = button.dataset.cvView;
      const active = target === view;
      button.setAttribute("aria-pressed", String(active));
      button.classList.toggle("is-active", active);
      if (button.dataset.cvReady === "true") return;
      button.dataset.cvReady = "true";
      button.addEventListener("click", () => {
        const next = new URL(window.location.href);
        next.searchParams.set("view", target);
        window.history.pushState({ cvView: target }, "", next.toString());
        initCvView();
      });
    });

    document.querySelectorAll("[data-current-view]").forEach((label) => {
      label.textContent = {
        ml: "ML/Data",
        agentic: "Agentic workflow",
        backend: "Backend/tooling",
        print: "Print"
      }[view];
    });
  }

  window.initCvView = initCvView;
  initCvView();
})();
