(function () {
  const allowed = new Set(["ml", "agentic", "backend", "print"]);
  const params = new URLSearchParams(window.location.search);
  const requested = params.get("view") || "agentic";
  const view = allowed.has(requested) ? requested : "agentic";
  document.documentElement.dataset.cvView = view;

  function appliesTo(node) {
    const views = (node.dataset.views || "").split(/\s+/).filter(Boolean);
    return views.length === 0 || views.includes(view) || view === "print";
  }

  document.querySelectorAll("[data-views]").forEach((node) => {
    node.hidden = !appliesTo(node);
  });

  document.querySelectorAll("button[data-cv-view]").forEach((button) => {
    const target = button.dataset.cvView;
    button.setAttribute("aria-pressed", String(target === view));
    button.addEventListener("click", () => {
      const next = new URL(window.location.href);
      next.searchParams.set("view", target);
      window.location.href = next.toString();
    });
  });

  const label = document.querySelector("[data-current-view]");
  if (label) {
    label.textContent = {
      ml: "ML/Data",
      agentic: "Agentic systems",
      backend: "Backend/tooling",
      print: "Print"
    }[view];
  }
})();
