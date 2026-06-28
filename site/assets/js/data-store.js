const SITE_ROOT = new URL("../../", import.meta.url);

const JSON_FILES = {
  site: "content/site.json",
  pages: "content/pages.json",
  projects: "content/projects.json",
  blog: "content/blog.json",
  cv: "content/cv.json"
};

const cache = new Map();

export function resolveSiteUrl(ref = "") {
  const value = String(ref || "");
  if (!value) return new URL(".", SITE_ROOT).href;
  if (/^(?:https?:|mailto:|tel:)/.test(value) || value.startsWith("#")) return value;
  return new URL(value.replace(/^\/+/, ""), SITE_ROOT).href;
}

export function hashHref(route = "/") {
  const clean = normalizeRoute(route);
  return `#${clean}`;
}

export function normalizeRoute(route = "/") {
  const raw = String(route || "/").trim();
  const withoutHash = raw.startsWith("#") ? raw.slice(1) : raw;
  const withoutQuery = withoutHash.split("?")[0].split("#")[0];
  let clean = withoutQuery.startsWith("/") ? withoutQuery : `/${withoutQuery}`;
  clean = clean.replace(/\/index\.html$/, "").replace(/\/+$/, "");
  return clean || "/";
}

export async function loadJson(ref) {
  const url = resolveSiteUrl(ref);
  if (!cache.has(url)) {
    cache.set(url, fetch(url, { credentials: "same-origin" }).then((response) => {
      if (!response.ok) throw new Error(`${ref} ${response.status}`);
      return response.json();
    }));
  }
  return cache.get(url);
}

export async function loadText(ref) {
  const url = resolveSiteUrl(ref);
  if (!cache.has(url)) {
    cache.set(url, fetch(url, { credentials: "same-origin" }).then((response) => {
      if (!response.ok) throw new Error(`${ref} ${response.status}`);
      return response.text();
    }));
  }
  return cache.get(url);
}

export async function loadContent() {
  const entries = await Promise.all(
    Object.entries(JSON_FILES).map(async ([key, ref]) => [key, await loadJson(ref)])
  );
  return Object.fromEntries(entries);
}
