import { normalizeRoute, resolveSiteUrl } from "./data-store.js";

const SITE_BASE_PATH = deploymentBasePath();

function deploymentBasePath() {
  const marker = "/assets/js/router.js";
  const path = new URL(import.meta.url).pathname;
  const markerIndex = path.lastIndexOf(marker);
  if (markerIndex < 0) return "/";
  const base = path.slice(0, markerIndex);
  return base ? `${base}/` : "/";
}

export function siteBasePath() {
  return SITE_BASE_PATH;
}

function stripDeploymentBase(pathname = "/") {
  const path = String(pathname || "/").replace(/\/index\.html$/, "/");
  if (SITE_BASE_PATH === "/") return path;
  const base = SITE_BASE_PATH.replace(/\/$/, "");
  if (path === base) return "/";
  if (path.startsWith(SITE_BASE_PATH)) return path.slice(base.length) || "/";
  return path;
}

export function routeFromLocation(location = window.location) {
  if (location.hash && location.hash.length > 1) return normalizeRoute(location.hash.slice(1));
  return normalizeRoute(stripDeploymentBase(location.pathname || "/"));
}

export function routeHref(route) {
  const normalized = normalizeRoute(route);
  if (normalized === "/") return SITE_BASE_PATH;
  return `${SITE_BASE_PATH.replace(/\/$/, "")}${normalized}`;
}

export function isStaticFileRoute(route = "") {
  return /^\/files\/[^?#]+\.[a-z0-9]+$/i.test(normalizeRoute(route));
}

export function redirectStaticFileRoute(route = "") {
  if (!isStaticFileRoute(route)) return false;
  window.location.replace(resolveSiteUrl(route));
  return true;
}

export function routeMatches(route, target) {
  const current = normalizeRoute(route);
  const cleanTarget = normalizeRoute(target);
  return current === cleanTarget || (cleanTarget !== "/" && current.startsWith(`${cleanTarget}/`));
}

export function bindRouter(callback) {
  window.addEventListener("popstate", () => callback(routeFromLocation()));
  window.addEventListener("hashchange", () => callback(routeFromLocation()));
  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[data-route], button[data-route]");
    if (!link) return;
    const route = normalizeRoute(link.dataset.route || link.getAttribute("href") || "/");
    if (isStaticFileRoute(route)) return;
    event.preventDefault();
    if (routeFromLocation() === route) {
      callback(route);
      return;
    }
    window.history.pushState({}, "", routeHref(route));
    callback(route);
  });
}
