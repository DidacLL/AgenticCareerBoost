const TAG_SEPARATOR = " · ";

export function buildGallerySlides(content = {}) {
  const manualSlides = Array.isArray(content?.site?.gallery)
    ? content.site.gallery.map(normalizeManualSlide)
    : [];
  const projectSlides = Array.isArray(content?.projects?.items)
    ? content.projects.items.map(projectToGallerySlide).filter(Boolean)
    : [];
  return [...manualSlides, ...projectSlides];
}

export function galleryLinks(slide = {}) {
  const explicit = Array.isArray(slide.links) ? slide.links : [];
  const links = explicit.length ? explicit : legacySlideLink(slide);
  return links.map(normalizeLink).filter(Boolean);
}

function normalizeManualSlide(slide = {}) {
  return {
    ...slide,
    lines: cleanLines(slide.lines),
    links: galleryLinks(slide)
  };
}

function projectToGallerySlide(project = {}, index = 0) {
  if (!project.image || !project.title || !project.route) return null;
  return {
    id: `project:${project.id || index + 1}`,
    kind: "project",
    projectId: project.id || "",
    label: `project.${project.id || index + 1}`,
    image: project.image,
    alt: project.alt || `${project.title} project preview`,
    title: project.title,
    route: project.route,
    lines: cleanLines([
      project.subtitle,
      Array.isArray(project.tags) ? project.tags.filter(Boolean).join(TAG_SEPARATOR) : ""
    ]),
    links: [{ label: "Open project", route: project.route }],
    caption: "project / selected work",
    contain: true
  };
}

function legacySlideLink(slide = {}) {
  if (!slide.route && !slide.href) return [];
  return [{
    label: slide.caption || slide.title || "",
    route: slide.route,
    href: slide.href,
    newTab: slide.newTab,
    download: slide.download
  }];
}

function normalizeLink(link = {}) {
  if (!link || (!link.route && !link.href)) return null;
  return {
    label: link.label || link.title || link.caption || "",
    route: link.route,
    href: link.href,
    newTab: link.newTab,
    download: link.download
  };
}

function cleanLines(lines = []) {
  return (Array.isArray(lines) ? lines : [lines])
    .map((line) => String(line || "").trim())
    .filter(Boolean);
}
