function wireMonitor(monitor) {
  if (monitor.dataset.monitorWired === "true") return;
  const slides = JSON.parse(monitor.dataset.monitorSlides || "[]");
  if (!slides.length) return;
  monitor.dataset.monitorWired = "true";

  let index = 0;
  const screen = monitor.querySelector("[data-monitor-screen]");
  const image = monitor.querySelector("[data-monitor-image]");
  const label = monitor.querySelector("[data-monitor-label]");
  const title = monitor.querySelector("[data-monitor-title]");
  const copy = monitor.querySelector("[data-monitor-copy]");
  const links = monitor.querySelector("[data-monitor-links]");
  const caption = monitor.querySelector("[data-monitor-caption]");
  const captionTitle = monitor.querySelector("[data-monitor-caption-title]");
  const position = monitor.querySelector("[data-monitor-position]");
  const expand = monitor.querySelector("[data-monitor-expand]");

  function applySlide(nextIndex) {
    index = (nextIndex + slides.length) % slides.length;
    const slide = slides[index];
    image.src = slide.image;
    image.alt = slide.alt || "";
    screen.classList.toggle("is-contained", Boolean(slide.contain));
    label.textContent = slide.label || "";
    title.textContent = slide.title || "";
    copy.textContent = (slide.lines || []).join(" · ");
    captionTitle.textContent = slide.title || "";
    caption.textContent = slide.caption || "";
    position.textContent = String(index + 1).padStart(2, "0");
    links.replaceChildren(...(slide.links || []).map((item) => {
      const link = document.createElement("a");
      link.href = item.href;
      link.textContent = item.label;
      if (item.external) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
      return link;
    }));
  }

  function setExpanded(expanded) {
    monitor.dataset.expanded = String(expanded);
    monitor.setAttribute("role", expanded ? "dialog" : "group");
    if (expanded) monitor.setAttribute("aria-modal", "true");
    else monitor.removeAttribute("aria-modal");
    expand.setAttribute("aria-expanded", String(expanded));
    expand.textContent = expanded ? expand.dataset.labelCollapse : expand.dataset.labelExpand;
    document.body.classList.toggle("monitor-open", expanded);
  }

  monitor.querySelector("[data-monitor-prev]")?.addEventListener("click", () => applySlide(index - 1));
  monitor.querySelector("[data-monitor-next]")?.addEventListener("click", () => applySlide(index + 1));
  expand?.addEventListener("click", () => setExpanded(monitor.dataset.expanded !== "true"));
}

function wireMonitors() {
  document.querySelectorAll("[data-monitor]").forEach(wireMonitor);
}

wireMonitors();
if (!window.__acbMonitorLifecycleWired) {
  window.__acbMonitorLifecycleWired = true;
  document.addEventListener("astro:page-load", wireMonitors);
  document.addEventListener("astro:before-swap", () => document.body.classList.remove("monitor-open"));
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    document.querySelector('[data-monitor][data-expanded="true"] [data-monitor-expand]')?.click();
  });
}
