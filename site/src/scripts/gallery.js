document.querySelectorAll("[data-gallery]").forEach((gallery) => {
  const image = gallery.querySelector("img");
  const expand = gallery.querySelector("[data-gallery-expand]");
  let index = 0;
  const labels = [image?.alt || "", "portrait / secondary signal"];
  const sync = () => {
    gallery.dataset.slide = String(index);
    if (image) image.alt = labels[index];
  };
  gallery.querySelector("[data-gallery-previous]")?.addEventListener("click", () => { index = (index + labels.length - 1) % labels.length; sync(); });
  gallery.querySelector("[data-gallery-next]")?.addEventListener("click", () => { index = (index + 1) % labels.length; sync(); });
  expand?.addEventListener("click", () => {
    const expanded = gallery.dataset.expanded !== "true";
    gallery.dataset.expanded = String(expanded);
    expand.textContent = expanded ? "minimize" : "maximize";
    expand.setAttribute("aria-expanded", String(expanded));
  });
  sync();
});
