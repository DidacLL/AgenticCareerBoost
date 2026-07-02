import { normalizeRoute } from "./data-store.js";

export function routeFromLocation(location = window.location) {
  if (location.hash && location.hash.length > 1) return normalizeRoute(location.hash.slice(1));
  return normalizeRoute(location.pathname || "/");
}

export function routeHref(route) {
  return normalizeRoute(route);
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
    event.preventDefault();
    if (routeFromLocation() === route) {
      callback(route);
      return;
    }
    window.history.pushState({}, "", route);
    callback(route);
  });
}
