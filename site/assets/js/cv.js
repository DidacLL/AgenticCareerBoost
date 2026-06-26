(function () {
  const allowed = new Set(["ml", "agentic", "backend", "print"]);

  function appliesTo(node, view) {
    const views = (node.dataset.views || "").split(/\s+/).filter(Boolean);
    return views.length === 0 || views.includes(view) || view === "print";
  }

  function initCvView() {
    const params = new URLSearchParams(window.location.search);
    const requested = params.get("view") || "ml";
    const view = allowed.has(requested) ? requested : "ml";
    document.documentElement.dataset.cvView = view;

    document.querySelectorAll("[data-views]").forEach((node) => {
      node.hidden = !appliesTo(node, view);
    });

    document.querySelectorAll("button[data-cv-view]").forEach((button) => {
      const target = button.dataset.cvView;
      button.setAttribute("aria-pressed", String(target === view));
      if (button.dataset.cvReady === "true") return;
      button.dataset.cvReady = "true";
      button.addEventListener("click", () => {
        const next = new URL(window.location.href);
        next.searchParams.set("view", target);
        window.location.href = next.toString();
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
