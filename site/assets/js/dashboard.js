(() => {
  const dashboardScript = document.currentScript ? new URL(document.currentScript.src) : null;
  const dashboardRoot = dashboardScript ? new URL("../..", dashboardScript) : new URL("./", window.location.href);
  const statusUrl = "assets/data/public-status.json";

  function statusHref() {
    return new URL(statusUrl, dashboardRoot).href;
  }

  function text(value, fallback = "Unavailable") {
    return value === null || value === undefined || value === "" ? fallback : String(value);
  }

  function renderArtifacts(root, artifacts = []) {
    const list = root.querySelector("[data-dashboard-artifacts]");
    if (!list) return;
    list.innerHTML = "";
    artifacts.forEach((artifact) => {
      const item = document.createElement("li");
      item.className = artifact.complete ? "is-complete" : "is-open";
      item.innerHTML = `<span>${artifact.complete ? "done" : "open"}</span><strong>${text(artifact.label)}</strong>`;
      list.appendChild(item);
    });
  }

  function renderBlockers(root, blockers = []) {
    const list = root.querySelector("[data-dashboard-blockers]");
    if (!list) return;
    list.innerHTML = "";
    const rows = blockers.length ? blockers : ["No current blockers exported."];
    rows.forEach((blocker) => {
      const item = document.createElement("li");
      item.textContent = blocker;
      list.appendChild(item);
    });
  }

  function renderDashboard(root, payload) {
    root.querySelectorAll("[data-status-field]").forEach((node) => {
      node.textContent = text(payload[node.dataset.statusField], node.dataset.fallback || "Unavailable");
    });

    const artifacts = Array.isArray(payload.artifacts) ? payload.artifacts : [];
    const complete = artifacts.filter((artifact) => artifact.complete).length;
    const total = artifacts.length || 1;
    const percent = Math.round((complete / total) * 100);
    root.style.setProperty("--dashboard-progress", `${percent}%`);

    const progress = root.querySelector("[data-dashboard-progress]");
    if (progress) progress.textContent = `${complete}/${artifacts.length || 0}`;

    renderArtifacts(root, artifacts);
    renderBlockers(root, Array.isArray(payload.blockers) ? payload.blockers : []);

    root.querySelectorAll("[data-status-source]").forEach((link) => {
      link.href = statusHref();
    });
    root.dataset.dashboardState = "ready";
  }

  async function init() {
    const dashboards = document.querySelectorAll("[data-dashboard-root]");
    if (!dashboards.length) return;
    try {
      const response = await fetch(statusHref(), { cache: "no-store" });
      if (!response.ok) throw new Error(`status ${response.status}`);
      const payload = await response.json();
      dashboards.forEach((root) => renderDashboard(root, payload));
    } catch {
      dashboards.forEach((root) => {
        root.dataset.dashboardState = "fallback";
        root.querySelectorAll("[data-status-field]").forEach((node) => {
          node.textContent = node.dataset.fallback || "Status unavailable";
        });
      });
    }
  }

  window.initProjectDashboard = init;
  init();
})();
