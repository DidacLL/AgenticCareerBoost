document.querySelectorAll("[data-monitor]").forEach((monitor) => {
  const slides = JSON.parse(monitor.dataset.slides || "[]");

  if (!slides.length) {
    return;
  }

  let index = 0;
  const image = monitor.querySelector("[data-monitor-image]");
  const caption = monitor.querySelector("[data-monitor-caption]");
  const label = monitor.querySelector("[data-monitor-label]");

  const sync = () => {
    const slide = slides[index];
    monitor.dataset.index = String(index);

    if (image) {
      image.src = slide.image;
      image.alt = slide.alt;
    }

    if (caption) {
      caption.textContent = slide.caption;
    }

    if (label) {
      label.textContent = slide.caption;
    }
  };

  monitor.querySelector("[data-monitor-prev]")?.addEventListener("click", () => {
    index = (index + slides.length - 1) % slides.length;
    sync();
  });

  monitor.querySelector("[data-monitor-next]")?.addEventListener("click", () => {
    index = (index + 1) % slides.length;
    sync();
  });

  monitor.querySelector("[data-monitor-expand]")?.addEventListener("click", (event) => {
    const expanded = monitor.dataset.expanded !== "true";
    monitor.dataset.expanded = String(expanded);
    event.currentTarget.textContent = expanded ? "minimize" : "maximize";
    event.currentTarget.setAttribute("aria-expanded", String(expanded));
  });
});
