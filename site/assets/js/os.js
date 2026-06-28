import { loadContent, normalizeRoute } from "./data-store.js";
import { bindRouter, routeFromLocation } from "./router.js";
import { renderRoute } from "./renderer.js";
import { initTheme, mountLegal, wireWidgets } from "./widgets.js";

let contentState = null;

async function boot() {
  contentState = await loadContent();
  initTheme(contentState);
  await mountLegal(contentState);
  bindRouter(renderCurrentRoute);
  await renderCurrentRoute(routeFromLocation());
}

async function renderCurrentRoute(route) {
  const normalized = normalizeRoute(route);
  try {
    await renderRoute(contentState, normalized);
    wireWidgets(contentState);
  } catch (error) {
    console.error(error);
    if (normalized !== "/") window.location.hash = "/";
  }
}

boot().catch((error) => {
  console.error(error);
  document.body.dataset.appError = "true";
});
