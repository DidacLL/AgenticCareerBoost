import { empty, renderBlocks, renderBreadcrumb, renderHeader, renderMeta, renderShell, syncLogos } from "./components.js";
import { normalizeRoute } from "./data-store.js";

export function resolvePage(content, route) {
  const normalized = normalizeRoute(route);
  const routeEntry = (content.site.routes || []).find((item) => normalizeRoute(item.path) === normalized)
    || (content.site.routes || []).find((item) => item.path === "/");
  if (!routeEntry) throw new Error("No route registry found");

  if (routeEntry.source === "pages") return { routeEntry, page: content.pages.pages[routeEntry.id] };
  if (routeEntry.source === "projects") return { routeEntry, page: projectPage(content, routeEntry.id) };
  if (routeEntry.source === "blog") return { routeEntry, page: blogPage(content, routeEntry.id) };
  if (routeEntry.source === "cv") return { routeEntry, page: cvPage(content.cv, routeEntry.id) };
  return { routeEntry, page: content.pages.pages.home };
}

export async function renderRoute(content, route) {
  const { routeEntry, page } = resolvePage(content, route);
  document.title = routeEntry.title || content.site.defaultTitle || document.title;
  syncMetadata(content, routeEntry);
  renderShell(content, routeEntry.path);

  const documentShell = document.querySelector("[data-os-document]");
  if (documentShell && page?.documentLabel) documentShell.setAttribute("aria-label", page.documentLabel);

  const pageSlot = document.querySelector("[data-page-content]");
  if (pageSlot) {
    empty(pageSlot).append(
      renderHeader(page.header || { title: routeEntry.title, subtitle: routeEntry.description }),
      renderBreadcrumb(page.breadcrumb || []),
      await renderBlocks(page.blocks || [], content)
    );
  }

  const metaSlot = document.querySelector("[data-os-meta]");
  if (metaSlot) empty(metaSlot).append(...renderMeta(page.meta || [], content));
  syncLogos(document, content);
}

function projectPage(content, id) {
  const projects = content.projects;
  if (id === "index") return projects.index;
  const item = (projects.items || []).find((project) => project.id === id);
  if (!item) return projects.index;
  const parent = registryRoute(content.site, "projects", "index");
  return {
    documentLabel: `${item.title} project`,
    meta: item.meta || [],
    header: { label: "PROJECT", title: item.title, subtitle: item.subtitle },
    breadcrumb: [
      homeCrumb(content.site),
      { label: parent?.label || projects.index?.header?.title || "", route: parent?.path || "/" },
      { label: item.title }
    ],
    blocks: item.blocks || []
  };
}

function blogPage(content, id) {
  const blog = content.blog;
  if (id === "index") return blog.index;
  const item = (blog.items || []).find((entry) => entry.id === id);
  if (!item) return blog.index;
  const parent = registryRoute(content.site, "blog", "index");
  return {
    documentLabel: item.documentLabel,
    meta: item.meta || [],
    header: { label: "BLOG", title: item.title, subtitle: item.subtitle },
    breadcrumb: [
      homeCrumb(content.site),
      { label: parent?.label || blog.index?.header?.title || "", route: parent?.path || "/" },
      { label: item.title }
    ],
    blocks: item.blocks || []
  };
}

function cvPage(cv, id) {
  const view = (cv.views || []).find((item) => item.id === id) || cv.views?.[0];
  return {
    documentLabel: view.documentLabel,
    meta: view.meta || [],
    header: view.header,
    breadcrumb: view.breadcrumb || [],
    blocks: [{ type: "panel", label: "03 / CV", title: "Role view", blocks: [{ type: "cvView", view }] }]
  };
}

function homeCrumb(site) {
  const home = registryRoute(site, "pages", "home");
  return { label: home?.label || site.identity?.title || "", route: home?.path || "/" };
}

function registryRoute(site, source, id) {
  return (site.routes || []).find((item) => item.source === source && item.id === id);
}

function syncMetadata(content, routeEntry) {
  setMeta("description", routeEntry.description || content.site.baseDescription || "");
  setMeta("og:title", routeEntry.title || content.site.defaultTitle || "", "property");
  setMeta("og:description", routeEntry.description || content.site.baseDescription || "", "property");
  setMeta("og:type", "profile", "property");
  setMeta("twitter:card", "summary_large_image");
  setMeta("twitter:title", routeEntry.title || content.site.defaultTitle || "");
  setMeta("twitter:description", routeEntry.description || content.site.baseDescription || "");
}

function setMeta(name, value, attr = "name") {
  let meta = document.head.querySelector(`meta[${attr}="${name}"]`);
  if (!meta) {
    meta = document.createElement("meta");
    meta.setAttribute(attr, name);
    document.head.append(meta);
  }
  meta.setAttribute("content", value);
}
