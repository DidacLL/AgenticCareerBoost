import { loadJson, loadText, resolveSiteUrl } from "./data-store.js";
import { buildGallerySlides, galleryLinks } from "./gallery-model.js";
import { routeHref, routeMatches } from "./router.js";

export function node(tag, attrs = {}, children = []) {
  const element = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs || {})) {
    if (value === false || value === null || value === undefined) continue;
    if (key === "class") element.className = value;
    else if (key === "text") element.textContent = value;
    else if (key === "html") element.innerHTML = value;
    else if (key.startsWith("data")) element.dataset[key.slice(4, 5).toLowerCase() + key.slice(5)] = value;
    else if (key.startsWith("aria")) {
      const name = key.replace(/[A-Z]/g, (letter) => `-${letter.toLowerCase()}`);
      element.setAttribute(name, String(value));
    }
    else element.setAttribute(key, String(value));
  }
  for (const child of Array.isArray(children) ? children : [children]) {
    if (child === null || child === undefined || child === false) continue;
    element.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
  return element;
}

export function empty(element) {
  element.replaceChildren();
  return element;
}

export function isExternalHref(href = "") {
  return /^(?:https?:)?\/\//.test(String(href || ""));
}

export function isStaticFileHref(href = "") {
  const value = String(href || "").split("#", 1)[0].split("?", 1)[0];
  return /^(?:\/)?files\/.+\.[a-z0-9]+$/i.test(value) || /\.(?:pdf|zip|txt|csv|json)$/i.test(value);
}

export function routeLink(item, className = "") {
  const hrefIsFile = isStaticFileHref(item.href);
  const href = item.route && !hrefIsFile ? routeHref(item.route) : resolveSiteUrl(item.href);
  const attrs = { href, class: className };
  if (item.route && !hrefIsFile) attrs.dataRoute = item.route;
  if (isExternalHref(item.href) || hrefIsFile || item.newTab) {
    attrs.target = "_blank";
    attrs.rel = "noopener noreferrer";
  }
  if (item.download) attrs.download = item.download === true ? "" : item.download;
  return node("a", attrs, item.label || item.title || href || "");
}

export function imageNode(item, content) {
  if (item.logo && content?.site?.logos?.[item.logo]) {
    const logo = content.site.logos[item.logo];
    const img = node("img", { alt: logo.alt || "", dataLogo: item.logo });
    syncLogo(img, logo);
    return img;
  }
  if (!item.image) return null;
  return node("img", { src: resolveSiteUrl(item.image), alt: item.alt || "" });
}

export function syncLogos(root = document, content) {
  root.querySelectorAll("img[data-logo]").forEach((img) => {
    const logo = content?.site?.logos?.[img.dataset.logo];
    if (logo) syncLogo(img, logo);
  });
}

function syncLogo(img, logo) {
  const theme = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
  const themed = logo.theme || logo;
  img.src = resolveSiteUrl(themed[theme] || themed.light || themed.dark || "");
  img.alt = logo.alt || img.alt || "";
}

export function renderHeader(header = {}) {
  return node("header", { class: "doc-header" }, [
    header.label ? node("p", { class: "os-label", text: header.label }) : null,
    node("h2", { text: header.title || "" }),
    header.subtitle ? node("p", { text: header.subtitle }) : null
  ]);
}

export function renderBreadcrumb(items = []) {
  if (!items.length) return null;
  const children = [];
  items.forEach((item, index) => {
    if (index) children.push(document.createTextNode(" / "));
    children.push(item.route || item.href ? routeLink(item) : node("span", { text: item.label || "" }));
  });
  return node("p", { class: "breadcrumb" }, children);
}

export async function renderBlocks(blocks = [], content) {
  const fragment = document.createDocumentFragment();
  for (const block of blocks) {
    const rendered = await renderBlock(block, content);
    if (rendered) fragment.append(rendered);
  }
  return fragment;
}

export async function renderBlock(block = {}, content) {
  const type = block.type || "prose";
  if (type === "panel") return renderTitledContainer("section", "os-panel is-active", block, content);
  if (type === "section") return renderTitledContainer("div", "os-section", block, content);
  if (type === "split") return renderSimpleContainer("div", block.layout === "intro" ? "intro-grid" : "preview-stack", block, content);
  if (type === "stack") return renderSimpleContainer("div", block.layout === "introCopy" ? "intro-copy" : "preview-stack", block, content);
  if (type === "prose") return renderProse(block);
  if (type === "facts") return renderFacts(block.items || []);
  if (type === "noteList") return renderNoteList(block.items || []);
  if (type === "previewList") return renderPreviewList(block.items || [], content, block.layout);
  if (type === "collectionList") return renderCollection(block, content);
  if (type === "statusDashboard") return renderStatusDashboard(block, content);
  if (type === "cvView") return renderCvView(block, content);
  if (type === "gallery") return renderGallery(content);
  if (type === "imageStrip") return renderImageStrip(block);
  if (type === "actions") return renderActions(block.items || []);
  if (type === "tags") return renderTags(block.items || []);
  if (type === "fragment") return renderFragment(block);
  return renderProse({ paragraphs: [block.text || ""] });
}

async function renderTitledContainer(tag, className, block, content) {
  const children = [];
  if (block.label || block.title) {
    children.push(node("div", { class: "section-title" }, [
      block.label ? node("p", { class: "os-label", text: block.label }) : null,
      block.title ? node("h3", { text: block.title }) : null
    ]));
  }
  children.push(await renderBlocks(block.blocks || [], content));
  return node(tag, { class: className }, children);
}

async function renderSimpleContainer(tag, className, block, content) {
  return node(tag, { class: className }, await renderBlocks(block.blocks || [], content));
}

function renderProse(block) {
  const children = [];
  if (block.lead) children.push(node("p", { class: "lead", text: block.lead }));
  (block.paragraphs || []).forEach((paragraph) => children.push(node("p", { text: paragraph })));
  return node("div", { class: "prose-block" }, children);
}

function renderFacts(items) {
  return node("dl", { class: "os-facts" }, items.map((item) => node("div", {}, [
    node("dt", { text: item.term || "" }),
    node("dd", { text: item.value || "" })
  ])));
}

function renderTags(items) {
  return node("div", { class: "tag-list" }, items.map((tag) => node("span", { class: "tag", text: tag })));
}

function renderActions(items) {
  return node("div", { class: "rail-links" }, items.map((item) => routeLink(item)));
}

function renderNoteList(items) {
  return node("div", { class: "note-list" }, items.map((item) => {
    const title = item.route || item.href ? routeLink({ ...item, label: item.title }) : node("strong", { text: item.title || "" });
    return node("div", { class: "note-item" }, [
      item.kicker || item.date ? node("span", { text: item.kicker || item.date || "" }) : null,
      node("div", {}, [
        node("h3", {}, [title]),
        item.text || item.summary ? node("p", { text: item.text || item.summary }) : null
      ])
    ]);
  }));
}

function renderPreviewList(items, content, layout = "") {
  const className = layout === "grid" ? "preview-list is-grid" : "preview-list";
  return node("div", { class: className }, items.map((item) => {
    const media = imageNode(item, content);
    const thumb = node("span", { class: "monitor-thumb" }, media ? [media] : []);
    const body = node("span", {}, [
      node("strong", { text: item.title || "" }),
      item.text || item.summary || item.subtitle ? node("small", { text: item.text || item.summary || item.subtitle }) : null,
      item.tags ? renderTags(item.tags) : null
    ]);
    const row = item.route || item.href ? routeLink({ ...item, label: "" }, "preview-row") : node("div", { class: "preview-row" });
    row.replaceChildren(thumb, body);
    return row;
  }));
}

function renderCollection(block, content) {
  const items = block.collection === "blog" ? content.blog.items : content.projects.items;
  if (block.layout === "previewList") return renderPreviewList(items, content);
  return renderNoteList(items);
}

function renderImageStrip(block) {
  return node("div", { class: "banner-strip" }, [
    node("img", { src: resolveSiteUrl(block.image), alt: block.alt || "" })
  ]);
}

function renderGalleryLinks(slide) {
  const links = galleryLinks(slide);
  return node("span", { class: "holo-links", dataGalleryLinks: "" }, links.map((item) => {
    const link = routeLink(item, "gallery-link");
    link.dataset.galleryLink = "";
    return link;
  }));
}

function renderGallery(content) {
  const slides = buildGallerySlides(content);
  const first = slides[0] || {};
  const copy = node("span", { dataGalleryCopy: "" });
  (first.lines || []).forEach((line, index) => {
    if (index) copy.append(node("br"));
    copy.append(line);
  });
  return node("figure", { class: "holo-window", dataHoloWindow: "", dataGalleryIndex: "0" }, [
    node("div", { class: "holo-toolbar" }, [
      node("button", { type: "button", class: "holo-step", dataGalleryPrev: "", ariaLabel: "Previous shortcut", text: "<" }),
      node("span", { dataGalleryLabel: "", text: first.label || "" }),
      node("button", { type: "button", class: "holo-step", dataGalleryNext: "", ariaLabel: "Next shortcut", text: ">" }),
      node("button", { type: "button", dataHoloToggle: "", ariaExpanded: "false", text: content.site.shell?.galleryToggleLabels?.expand || "" })
    ]),
    node("div", { class: first.contain ? "holo-screen is-gallery-project" : "holo-screen" }, [
      node("img", { dataGalleryImage: "", src: first.image ? resolveSiteUrl(first.image) : "", alt: first.alt || "" }),
      node("div", { class: "holo-overlay", ariaHidden: "true" }, [
        node("strong", { dataGalleryTitle: "", text: first.title || "" }),
        copy,
        renderGalleryLinks(first)
      ])
    ]),
    node("figcaption", {}, [node("span", { dataGalleryCaption: "", text: first.caption || "" })])
  ]);
}

async function renderFragment(block) {
  const wrapper = node("div", { class: "fragment-block" });
  wrapper.innerHTML = await loadText(block.src);
  return wrapper;
}

async function renderStatusDashboard(block, content) {
  const status = await loadJson(block.status);
  const labels = content.site.shell?.dashboardLabels || {};
  const view = { ...(content.site.shell?.dashboardPresentation || {}), ...(block.presentation || {}) };
  const complete = (status.artifacts || []).filter((item) => item.complete).length;
  const total = (status.artifacts || []).length || 1;
  const progress = Math.round((complete / total) * 100);
  const doneItems = (status.artifacts || []).filter((item) => item.complete);
  const openItems = (status.artifacts || []).filter((item) => !item.complete);
  const blockers = status.blockers || [];
  return node("div", { class: "project-dashboard" }, [
    block.label || block.title ? node("div", { class: "section-title" }, [
      block.label ? node("p", { class: "os-label", text: block.label }) : null,
      block.title ? node("h3", { text: block.title }) : null
    ]) : null,
    node("div", { class: "dashboard-grid" }, [
      metric(labels.purpose || "", view.purpose || ""),
      metric(labels.state || "", statusText(status, view)),
      metric(labels.lastClosure || "", [status.last_closure_type, status.last_closure_at].filter(Boolean).join(" · ")),
      metric(labels.next || "", status.next_sprint_seed || "")
    ]),
    node("div", { class: "dashboard-meter" }, [
      node("span", { style: `width:${progress}%` }),
      node("strong", { text: `${complete}/${total}` }),
      node("small", { text: `${labels.progress || ""} · ${complete} ${view.progressSuffix || ""}` })
    ]),
    node("div", { class: "dashboard-columns" }, [
      node("section", {}, [
        node("p", { class: "os-label", text: labels.done || "" }),
        dashboardList(doneItems, labels.complete || "")
      ]),
      node("section", {}, [
        node("p", { class: "os-label", text: labels.needsHuman || "" }),
        dashboardList(blockers.length ? blockers.map((label) => ({ label, complete: false })) : openItems, labels.incomplete || "", view.emptyBlockers)
      ])
    ]),
    node("div", { class: "os-section dashboard-evidence" }, [
      node("div", { class: "section-title" }, [
        node("p", { class: "os-label", text: labels.evidence || "" }),
        node("h3", { text: labels.evidence || "" })
      ]),
      node("ul", { class: "file-list" }, (view.evidenceLinks || []).map((link) => node("li", {}, [routeLink(link)])))
    ])
  ]);
}

function statusText(status, view) {
  const workflow = view.workflowLabels?.[status.workflow] || status.workflow || "";
  const state = view.stateLabels?.[status.status] || status.status || "";
  return [workflow, state].filter(Boolean).join(" · ");
}

function dashboardList(items, stateLabel, emptyText = "") {
  if (!items.length && emptyText) {
    return node("ul", { class: "dashboard-list is-blockers" }, [
      node("li", {}, [
        node("span", { text: stateLabel }),
        node("strong", { text: emptyText })
      ])
    ]);
  }
  return node("ul", { class: "dashboard-list" }, items.map((item) => node("li", {
    class: item.complete ? "is-complete" : "is-open"
  }, [
    node("span", { text: stateLabel }),
    node("strong", { text: readableStatusItem(item.label || "") })
  ])));
}

function readableStatusItem(label) {
  const afterDash = label.includes("—") ? label.split("—").slice(1).join("—") : label;
  const afterColon = afterDash.includes(":") ? afterDash.split(":").slice(1).join(":") : afterDash;
  return afterColon.replace(/`/g, "").trim() || label;
}

function metric(term, value) {
  return node("div", { class: "dashboard-tile" }, [
    node("span", { class: "os-label", text: term }),
    node("strong", { text: value })
  ]);
}

function renderCvView(block, content) {
  const view = block.view;
  const views = content.cv.views || [];
  const labels = content.cv.sectionLabels || {};
  return node("section", { class: "cv-module", dataCvView: view.id }, [
    node("div", { class: "cv-toolbar" }, [
      node("div", { class: "segmented" }, views.map((item) => {
      const button = node("button", {
        type: "button",
        class: item.id === view.id ? "is-active" : "",
        dataRoute: `/cv/${item.id}`,
        ariaPressed: String(item.id === view.id),
        text: item.label
      });
      return button;
      }))
    ]),
    (() => {
      const artifacts = renderPreviewList(content.cv.artifacts || [], content);
      artifacts.classList.add("cv-artifacts");
      return artifacts;
    })(),
    node("div", { class: "os-section" }, [
      node("div", { class: "section-title" }, [
        node("p", { class: "os-label", text: labels.profile?.label || "" }),
        node("h3", { text: labels.profile?.title || "" })
      ]),
      renderProse({ paragraphs: view.profile || [] })
    ]),
    node("div", { class: "os-section" }, [
      node("div", { class: "section-title" }, [
        node("p", { class: "os-label", text: labels.lanes?.label || "" }),
        node("h3", { text: labels.lanes?.title || "" })
      ]),
      renderTags(view.lanes || [])
    ]),
    node("div", { class: "os-section" }, [
      node("div", { class: "section-title" }, [
        node("p", { class: "os-label", text: labels.work?.label || "" }),
        node("h3", { text: labels.work?.title || "" })
      ]),
      renderPreviewList(content.cv.selectedWork || [], content)
    ]),
    node("div", { class: "os-section" }, [
      node("div", { class: "section-title" }, [
        node("p", { class: "os-label", text: labels.base?.label || "" }),
        node("h3", { text: labels.base?.title || "" })
      ]),
      renderFacts(view.technicalBase || [])
    ])
  ]);
}

export function renderMeta(sections = [], content) {
  return sections.map((section) => node("section", {}, [
    node("p", { class: "os-label", text: section.label || "" }),
    section.rows ? node("dl", { class: "meta-list" }, section.rows.map((row) => node("div", {}, [
      node("dt", { text: row.term || "" }),
      node("dd", {}, [row.control === "themeToggle" ? node("button", { class: "theme-toggle", type: "button", dataThemeToggle: "", text: "" }) : row.link ? routeLink(row.link) : row.value || ""])
    ]))) : null,
    section.links ? node("ul", { class: "file-list" }, section.links.map((link) => node("li", {}, [routeLink(link)]))) : null,
    section.previews ? renderMiniPreviews(section.previews, content) : null,
    section.tags ? renderTags(section.tags) : null
  ]));
}

function renderMiniPreviews(items = [], content) {
  return node("div", { class: "preview-stack" }, items.map((item) => {
    const link = routeLink({ ...item, label: "" }, "mini-monitor");
    const media = imageNode(item, content);
    link.replaceChildren(media || "", node("span", { text: item.label || item.title || "" }));
    return link;
  }));
}

export function renderShell(content, activeRoute) {
  const site = content.site;
  const identity = site.identity || {};
  const nav = site.nav?.primary || [];
  const external = site.nav?.external || [];
  const rail = document.querySelector("[data-os-rail]");
  if (rail) {
    empty(rail).append(
      node("div", { class: "identity-block" }, [
        node("span", { class: "os-mark", text: identity.mark || "" }),
        node("h1", { id: "identity-title", text: identity.title || "" }),
        ...(identity.lines || []).map((line) => node("p", { text: line }))
      ]),
      node("nav", { class: "os-nav", ariaLabel: "Primary navigation" }, nav.map((item) => {
        const link = routeLink(item);
        link.replaceChildren(node("span", { text: item.number || "" }), document.createTextNode(` ${item.label || ""}`));
        if (routeMatches(activeRoute, item.route)) link.classList.add("is-active");
        if (routeMatches(activeRoute, item.route)) link.setAttribute("aria-current", "page");
        return link;
      })),
      node("div", { class: "rail-links", ariaLabel: "External links" }, external.map((item) => routeLink(item)))
    );
  }
  const tabs = document.querySelector("[data-doc-tabs]");
  if (tabs) {
    empty(tabs).append(...nav.map((item) => {
      const link = routeLink(item);
      if (routeMatches(activeRoute, item.route)) link.classList.add("is-active");
      if (routeMatches(activeRoute, item.route)) link.setAttribute("aria-current", "page");
      return link;
    }));
  }
  const banner = document.querySelector("[data-system-banner]");
  if (banner && site.shell?.bannerImage) {
    empty(banner).append(node("img", { src: resolveSiteUrl(site.shell.bannerImage), alt: site.shell.bannerAlt || "" }));
  }
}
