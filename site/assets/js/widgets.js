import { loadText, resolveSiteUrl } from "./data-store.js";
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
  const slides = content.site.gallery || [];
  if (!slides.length) return;
  const nextIndex = (index + slides.length) % slides.length;
  const slide = slides[nextIndex];
  gallery.dataset.galleryIndex = String(nextIndex);

  const image = gallery.querySelector("[data-gallery-image]");
  const screen = gallery.querySelector(".holo-screen");
  const label = gallery.querySelector("[data-gallery-label]");
  const title = gallery.querySelector("[data-gallery-title]");
  const copy = gallery.querySelector("[data-gallery-copy]");
  const link = gallery.querySelector("[data-gallery-link]");
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
  if (link) {
    const hrefIsFile = isStaticFileHref(slide.href);
    const href = slide.route && !hrefIsFile ? routeHref(slide.route) : resolveSiteUrl(slide.href || "");
    link.href = href;
    if (slide.route && !hrefIsFile) link.dataset.route = slide.route;
    else delete link.dataset.route;
    if (isExternalHref(slide.href) || hrefIsFile || slide.newTab) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    } else {
      link.removeAttribute("target");
      link.removeAttribute("rel");
    }
    link.textContent = slide.caption || slide.title || "";
  }
  if (caption) caption.textContent = slide.caption || "";
  if (toggle) toggle.textContent = gallery.classList.contains("is-expanded") ? labels.collapse || "" : labels.expand || "";
}
