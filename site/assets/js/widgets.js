import { loadText, resolveSiteUrl } from "./data-store.js";
import { buildGallerySlides, galleryLinks } from "./gallery-model.js";
import { routeHref } from "./router.js";
import { isExternalHref, isStaticFileHref, syncLogos } from "./components.js";

const THEME_KEY = "didac-os-theme";

export function initTheme(content) {
  const stored = localStorage.getItem(THEME_KEY);
  const fallback = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  setTheme(stored === "light" || stored === "dark" ? stored : fallback, content, false);
}

export function wireWidgets(content) {
  wireThemeToggles(content);
  wireGallery(content);
}

export async function mountLegal(content) {
  const slot = document.querySelector("[data-legal-disclosure]");
  const src = content.site.shell?.legalFragment;
  if (!slot || !src) return;
  const html = await loadText(src);
  slot.outerHTML = html;
}

function wireThemeToggles(content) {
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    if (!button.dataset.boundTheme) {
      button.dataset.boundTheme = "true";
      button.addEventListener("click", () => {
        const current = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
        setTheme(current === "dark" ? "light" : "dark", content);
      });
    }
    labelThemeButton(button, content);
  });
}

function setTheme(theme, content, persist = true) {
  const next = theme === "dark" ? "dark" : "light";
  document.documentElement.dataset.theme = next;
  if (persist) localStorage.setItem(THEME_KEY, next);
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => labelThemeButton(button, content));
  syncLogos(document, content);
}

function labelThemeButton(button, content) {
  const theme = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
  const labels = content.site.shell?.themeToggleLabels || {};
  button.textContent = theme === "dark" ? labels.light || "" : labels.dark || "";
  button.setAttribute("aria-pressed", String(theme === "dark"));
}

function wireGallery(content) {
  document.querySelectorAll("[data-holo-window]").forEach((gallery) => {
    if (!gallery.dataset.galleryReady) applyGallerySlide(gallery, content, 0);
    gallery.dataset.galleryReady = "true";
    gallery.querySelectorAll("[data-gallery-prev], [data-gallery-next]").forEach((button) => {
      if (button.dataset.boundGallery) return;
      button.dataset.boundGallery = "true";
      button.addEventListener("click", () => {
        const current = Number(gallery.dataset.galleryIndex || "0");
        const delta = button.hasAttribute("data-gallery-next") ? 1 : -1;
        applyGallerySlide(gallery, content, current + delta);
      });
    });
    const toggle = gallery.querySelector("[data-holo-toggle]");
    if (toggle && !toggle.dataset.boundHolo) {
      toggle.dataset.boundHolo = "true";
      toggle.addEventListener("click", () => {
        const expanded = gallery.classList.toggle("is-expanded");
        const labels = content.site.shell?.galleryToggleLabels || {};
        toggle.textContent = expanded ? labels.collapse || "" : labels.expand || "";
        toggle.setAttribute("aria-expanded", String(expanded));
      });
    }
  });
}

function applyGallerySlide(gallery, content, index) {
  const slides = buildGallerySlides(content);
  if (!slides.length) return;
  const nextIndex = (index + slides.length) % slides.length;
  const slide = slides[nextIndex];
  gallery.dataset.galleryIndex = String(nextIndex);

  const image = gallery.querySelector("[data-gallery-image]");
  const screen = gallery.querySelector(".holo-screen");
  const label = gallery.querySelector("[data-gallery-label]");
  const title = gallery.querySelector("[data-gallery-title]");
  const copy = gallery.querySelector("[data-gallery-copy]");
  const links = gallery.querySelector("[data-gallery-links]");
  const legacyLink = links ? null : gallery.querySelector("[data-gallery-link]");
  const caption = gallery.querySelector("[data-gallery-caption]");
  const toggle = gallery.querySelector("[data-holo-toggle]");
  const labels = content.site.shell?.galleryToggleLabels || {};

  if (image) {
    image.src = resolveSiteUrl(slide.image || "");
    image.alt = slide.alt || "";
  }
  if (screen) screen.classList.toggle("is-gallery-project", Boolean(slide.contain));
  if (label) label.textContent = slide.label || "";
  if (title) title.textContent = slide.title || "";
  if (copy) {
    copy.replaceChildren();
    (slide.lines || []).forEach((line, lineIndex) => {
      if (lineIndex) copy.append(document.createElement("br"));
      copy.append(line);
    });
  }
  if (links) {
    links.replaceChildren(...galleryLinks(slide).map((item) => galleryLinkElement(item, slide)));
  } else if (legacyLink) {
    applyLink(legacyLink, galleryLinks(slide)[0] || {}, slide);
  }
  if (caption) caption.textContent = slide.caption || "";
  if (toggle) toggle.textContent = gallery.classList.contains("is-expanded") ? labels.collapse || "" : labels.expand || "";
}

function galleryLinkElement(item, slide) {
  const link = document.createElement("a");
  link.className = "gallery-link";
  link.dataset.galleryLink = "";
  applyLink(link, item, slide);
  return link;
}

function applyLink(link, item = {}, slide = item) {
  link.href = galleryHref(item, slide);
  const hrefIsFile = isStaticFileHref(item.href);
  const route = item.route || (!item.href ? slide.route : "");
  if (route && !hrefIsFile) link.dataset.route = route;
  else delete link.dataset.route;
  if (isExternalHref(item.href) || hrefIsFile || item.newTab) {
    link.target = "_blank";
    link.rel = "noopener noreferrer";
  } else {
    link.removeAttribute("target");
    link.removeAttribute("rel");
  }
  if (item.download) link.download = item.download === true ? "" : item.download;
  else link.removeAttribute("download");
  link.textContent = item.label || item.title || slide.caption || slide.title || "";
}

function galleryHref(item = {}, slide = item) {
  const hrefIsFile = isStaticFileHref(item.href);
  if (item.route && !hrefIsFile) return routeHref(item.route);
  if (!item.href && slide.route && !hrefIsFile) return routeHref(slide.route);
  return resolveSiteUrl(item.href || "");
}
