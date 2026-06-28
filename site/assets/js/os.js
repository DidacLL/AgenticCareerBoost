(() => {
  const osScript = document.currentScript ? new URL(document.currentScript.src) : null;
  const assetBase = osScript ? new URL(".", osScript) : null;
  const canonicalPanels = {
    intro: "index.html",
    home: "index.html",
    work: "projects/index.html",
    projects: "projects/index.html",
    now: "index.html",
    cv: "curriculum/index.html?view=ml",
    notes: "blog/index.html",
    blog: "blog/index.html",
    hire: "hire/index.html",
    contact: "contact/index.html",
  };

  const params = new URLSearchParams(window.location.search);
  const requestedPanel = params.get("panel");
  const isRootIndex = /(?:^|\/)(?:index\.html)?$/.test(window.location.pathname) &&
    !/\/(?:projects|blog|curriculum|notes|hire|contact|dashboard)\//.test(window.location.pathname);

  if (isRootIndex && requestedPanel && canonicalPanels[requestedPanel]) {
    window.location.replace(canonicalPanels[requestedPanel]);
    return;
  }

  function preferredTheme() {
    const stored = localStorage.getItem("didac-os-theme");
    if (stored === "light" || stored === "dark") return stored;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function setTheme(theme, persist = true) {
    const nextTheme = theme === "dark" ? "dark" : "light";
    document.documentElement.dataset.theme = nextTheme;
    if (persist) localStorage.setItem("didac-os-theme", nextTheme);
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.textContent = nextTheme === "dark" ? themeToggleLabels.light : themeToggleLabels.dark;
      button.setAttribute("aria-pressed", String(nextTheme === "dark"));
    });
    if (siteContentCache) siteContentCache.then(syncThemeLogos).catch(() => {});
  }

  function siteRoot() {
    if (assetBase) return new URL("../..", assetBase);
    return new URL(".", window.location.href);
  }

  function siteUrl(path = "") {
    const cleanPath = String(path || "").replace(/^\/+/, "");
    return new URL(cleanPath, siteRoot()).href;
  }

  let siteContentCache = null;
  let pagesContentCache = null;
  let legalFragmentCache = null;
  let gallerySlides = [];
  let themeToggleLabels = { dark: "", light: "" };

  function loadSiteContent() {
    if (!siteContentCache) {
      siteContentCache = fetch(siteUrl("assets/data/site-content.json"), { credentials: "same-origin" })
        .then((response) => {
          if (!response.ok) throw new Error(`site content ${response.status}`);
          return response.json();
        });
    }
    return siteContentCache;
  }

  function loadPagesContent(data) {
    if (!pagesContentCache) {
      pagesContentCache = fetch(siteUrl(data?.pagesData || "assets/data/pages.json"), { credentials: "same-origin" })
        .then((response) => {
          if (!response.ok) throw new Error(`page content ${response.status}`);
          return response.json();
        });
    }
    return pagesContentCache;
  }

  function currentRoutePath(url = window.location.href) {
    const route = new URL(url, window.location.href);
    const rootPath = siteRoot().pathname;
    let relative = route.pathname.startsWith(rootPath)
      ? route.pathname.slice(rootPath.length)
      : route.pathname.replace(/^\/+/, "");
    relative = relative.replace(/index\.html$/, "");
    if (relative && !relative.endsWith("/")) relative += "/";
    return `/${relative}`;
  }

  function pageContent(data, url = window.location.href) {
    const pages = data?.pages || {};
    const path = currentRoutePath(url);
    return pages[path] || pages[path.replace(/\/$/, "")] || pages["/"] || {};
  }

  function activeRoutePath(url = window.location.href) {
    const path = currentRoutePath(url);
    if (path.startsWith("/projects/")) return "/projects/";
    if (path.startsWith("/blog/")) return "/blog/";
    if (path.startsWith("/hire/")) return "/curriculum/";
    return path;
  }

  function escapeHtml(value = "") {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function escapeAttr(value = "") {
    return escapeHtml(value).replace(/'/g, "&#39;");
  }

  function navLink(route, compact = false) {
    const active = activeRoutePath() === route.path;
    const attrs = active ? ' class="is-active" aria-current="page"' : "";
    const label = compact
      ? escapeHtml(route.label)
      : `<span>${escapeHtml(route.number)}</span> ${escapeHtml(route.label)}`;
    return `<a${attrs} href="${siteUrl(route.href)}">${label}</a>`;
  }

  function renderSharedNavigation(data) {
    const routes = data?.nav?.primaryRoutes || [];
    const identity = data?.identity || {};
    const externalLinks = data?.nav?.externalLinks || [];
    const identityLines = (identity.lines || [])
      .map((line) => `<p>${escapeHtml(line)}</p>`)
      .join("");
    const railLinks = externalLinks
      .map((link) => `<a href="${siteUrl(link.href || "")}" target="_blank" rel="noopener noreferrer">${escapeHtml(link.label)}</a>`)
      .join("");
    document.querySelectorAll("[data-os-rail]").forEach((rail) => {
      rail.innerHTML = `<div class="identity-block"><span class="os-mark">${escapeHtml(identity.mark)}</span><h1 id="identity-title">${escapeHtml(identity.title)}</h1>${identityLines}</div><nav class="os-nav" aria-label="Primary navigation">${routes.map((route) => navLink(route)).join("")}</nav><div class="rail-links" aria-label="External links">${railLinks}</div>`;
    });
    document.querySelectorAll("[data-doc-tabs]").forEach((tabs) => {
      tabs.innerHTML = routes.map((route) => navLink(route, true)).join("");
    });
  }

  async function renderRouteContent(data, url = window.location.href) {
    const pages = await loadPagesContent(data);
    const route = pages?.routes?.[currentRoutePath(url)] || pages?.routes?.["/"];
    if (!route) throw new Error("Route content missing");
    document.querySelectorAll("[data-page-content]").forEach((slot) => {
      slot.innerHTML = route.contentHtml || "";
    });
    document.querySelectorAll("[data-os-meta]").forEach((slot) => {
      slot.innerHTML = route.metaHtml || "";
    });
    document.querySelectorAll("[data-os-document]").forEach((section) => {
      if (route.documentLabel) section.setAttribute("aria-label", route.documentLabel);
    });
  }

  function hydrateSystemBanner(data) {
    const banner = data?.shell || {};
    const image = banner.bannerImage;
    document.querySelectorAll("[data-system-banner]").forEach((slot) => {
      if (!image) return;
      let img = slot.querySelector("img");
      if (!img) {
        img = document.createElement("img");
        slot.appendChild(img);
      }
      img.src = siteUrl(image);
      img.alt = banner.bannerAlt || "";
    });
  }

  function ensureHeadElement(selector, create) {
    let node = document.head.querySelector(selector);
    if (!node) {
      node = create();
      document.head.appendChild(node);
    }
    return node;
  }

  function ensureMetaByName(name) {
    return ensureHeadElement(`meta[name="${name}"]`, () => {
      const meta = document.createElement("meta");
      meta.setAttribute("name", name);
      return meta;
    });
  }

  function ensureMetaByProperty(property) {
    return ensureHeadElement(`meta[property="${property}"]`, () => {
      const meta = document.createElement("meta");
      meta.setAttribute("property", property);
      return meta;
    });
  }

  function syncPageMetadata(data, url = window.location.href) {
    const page = pageContent(data, url);
    const canonicalPath = page.canonicalPath || currentRoutePath(url);
    const title = page.title || data?.defaultTitle || document.title || "";
    const description = page.description || data?.site?.description || "";
    const image = page.image || "assets/img/avatar.jpg";

    document.title = title;
    ensureMetaByName("description").setAttribute("content", description);
    ensureMetaByProperty("og:type").setAttribute("content", page.type || "profile");
    ensureMetaByProperty("og:title").setAttribute("content", title);
    ensureMetaByProperty("og:description").setAttribute("content", description);
    ensureMetaByProperty("og:url").dataset.siteUrl = "canonical";
    ensureMetaByProperty("og:image").dataset.siteImage = image;
    ensureMetaByName("twitter:card").setAttribute("content", "summary_large_image");
    ensureMetaByName("twitter:title").setAttribute("content", title);
    ensureMetaByName("twitter:description").setAttribute("content", description);
    ensureMetaByName("twitter:image").dataset.siteImage = image;

    const canonical = ensureHeadElement('link[rel="canonical"]', () => {
      const link = document.createElement("link");
      link.setAttribute("rel", "canonical");
      return link;
    });
    canonical.dataset.canonicalPath = canonicalPath;
    syncRuntimeUrls();
  }

  async function hydrateLegalDisclosure(data) {
    const slots = document.querySelectorAll("[data-legal-disclosure]");
    if (!slots.length || !data?.legalFragment) return;
    if (!legalFragmentCache) {
      const response = await fetch(siteUrl(data.legalFragment), { credentials: "same-origin" });
      if (!response.ok) throw new Error(`legal fragment ${response.status}`);
      legalFragmentCache = await response.text();
    }
    slots.forEach((slot) => {
      slot.outerHTML = legalFragmentCache;
    });
  }

  function syncThemeLogos(data) {
    const theme = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
    const logos = data?.logos || {};
    document.querySelectorAll("img[data-logo]").forEach((img) => {
      const logo = logos[img.dataset.logo];
      if (!logo) return;
      img.src = siteUrl(logo[theme] || logo.light || logo.dark || "");
      img.alt = logo.alt || img.alt || "";
    });
  }

  async function hydrateSharedContent(url = window.location.href) {
    const data = await loadSiteContent();
    gallerySlides = data?.gallerySlides || [];
    themeToggleLabels = data?.shell?.themeToggleLabels || themeToggleLabels;
    syncPageMetadata(data, url);
    renderSharedNavigation(data);
    hydrateSystemBanner(data);
    await renderRouteContent(data, url);
    await hydrateLegalDisclosure(data);
    syncThemeLogos(data);
    wireThemeToggles();
    wireSignalGalleries();
    wireHoloWindows();
    secureExternalLinks();
    await ensureCvScript(new URL(url, window.location.href).pathname);
    await ensureDashboardScript(new URL(url, window.location.href).pathname);
    return data;
  }

  function syncRuntimeUrls(root = document) {
    root.querySelectorAll('link[rel="canonical"][data-canonical-path]').forEach((link) => {
      link.href = siteUrl(link.dataset.canonicalPath || "");
    });

    const canonical = root.querySelector('link[rel="canonical"]') || document.querySelector('link[rel="canonical"]');
    const canonicalHref = canonical?.href || window.location.href;
    root.querySelectorAll('meta[data-site-url="canonical"]').forEach((meta) => {
      meta.setAttribute("content", canonicalHref);
    });

    root.querySelectorAll("meta[data-site-image]").forEach((meta) => {
      meta.setAttribute("content", siteUrl(meta.dataset.siteImage || ""));
    });
  }

  function wireThemeToggles(root = document) {
    root.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      if (button.dataset.osReady === "theme") return;
      button.dataset.osReady = "theme";
      button.addEventListener("click", () => {
        const current = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
        setTheme(current === "dark" ? "light" : "dark");
      });
      const current = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
      button.textContent = current === "dark" ? themeToggleLabels.light : themeToggleLabels.dark;
      button.setAttribute("aria-pressed", String(current === "dark"));
    });
  }

  function secureExternalLinks(root = document) {
    root.querySelectorAll('a[href^="http://"], a[href^="https://"]').forEach((link) => {
      const url = new URL(link.href, window.location.href);
      if (url.origin === window.location.origin) return;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    });
  }

  function applyGallerySlide(windowNode, index) {
    if (!gallerySlides.length) return;
    const nextIndex = (index + gallerySlides.length) % gallerySlides.length;
    const slide = gallerySlides[nextIndex];
    windowNode.dataset.galleryIndex = String(nextIndex);

    const image = windowNode.querySelector("[data-gallery-image]");
    const screen = windowNode.querySelector(".holo-screen");
    const label = windowNode.querySelector("[data-gallery-label]");
    const title = windowNode.querySelector("[data-gallery-title]");
    const copy = windowNode.querySelector("[data-gallery-copy]");
    const link = windowNode.querySelector("[data-gallery-link]");
    const caption = windowNode.querySelector("[data-gallery-caption]");

    if (image) {
      image.src = slide.image;
      image.alt = slide.alt;
    }
    if (screen) screen.classList.toggle("is-gallery-project", slide.project);
    if (label) label.textContent = slide.label;
    if (title) title.textContent = slide.title;
    if (copy) copy.innerHTML = slide.copy;
    if (link) link.href = slide.href;
    if (caption) caption.textContent = slide.caption;
  }

  function wireSignalGalleries(root = document) {
    root.querySelectorAll("[data-holo-window]").forEach((windowNode) => {
      if (!windowNode.dataset.galleryIndex) applyGallerySlide(windowNode, 0);
      windowNode.querySelectorAll("[data-gallery-prev], [data-gallery-next]").forEach((button) => {
        if (button.dataset.osReady === "gallery") return;
        button.dataset.osReady = "gallery";
        button.addEventListener("click", () => {
          const current = Number(windowNode.dataset.galleryIndex || "0");
          applyGallerySlide(windowNode, current + (button.hasAttribute("data-gallery-next") ? 1 : -1));
        });
      });
    });
  }

  function wireHoloWindows(root = document) {
    root.querySelectorAll("[data-holo-toggle]").forEach((button) => {
      if (button.dataset.osReady === "holo") return;
      button.dataset.osReady = "holo";
      button.addEventListener("click", () => {
        const windowNode = button.closest("[data-holo-window]");
        if (!windowNode) return;
        const expanded = windowNode.classList.toggle("is-expanded");
        if (!expanded) applyGallerySlide(windowNode, 0);
        button.setAttribute("aria-expanded", String(expanded));
        button.textContent = expanded ? "minimize" : "maximize";
      });
      const windowNode = button.closest("[data-holo-window]");
      button.setAttribute("aria-expanded", String(windowNode?.classList.contains("is-expanded")));
    });
  }

  function internalHtmlTarget(link) {
    if (window.location.protocol === "file:") return null;
    if (link.target || link.hasAttribute("download")) return null;

    const url = new URL(link.getAttribute("href"), window.location.href);
    if (url.origin !== window.location.origin) return null;
    if (url.hash && url.pathname === window.location.pathname) return null;
    if (!/\/(?:index\.html)?$/.test(url.pathname) && !/\.html$/.test(url.pathname)) return null;
    if (/\.(pdf|tex|json|png|jpg|jpeg|webp|svg)$/i.test(url.pathname)) return null;
    return url;
  }

  function isCvPath(pathname = window.location.pathname) {
    return /\/curriculum\/(?:index\.html)?$/.test(pathname);
  }

  async function ensureCvScript(pathname = window.location.pathname) {
    if (!isCvPath(pathname)) return;
    if (window.initCvView) {
      window.initCvView();
      return;
    }
    const existing = document.querySelector('script[data-cv-runtime="true"]');
    if (existing) {
      await new Promise((resolve) => existing.addEventListener("load", resolve, { once: true }));
      if (window.initCvView) window.initCvView();
      return;
    }
    await new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.defer = true;
      script.dataset.cvRuntime = "true";
      script.src = assetBase ? new URL("cv.js", assetBase).href : "assets/js/cv.js";
      script.addEventListener("load", resolve, { once: true });
      script.addEventListener("error", reject, { once: true });
      document.head.appendChild(script);
    });
    if (window.initCvView) window.initCvView();
  }

  function needsDashboard(pathname = window.location.pathname) {
    return /\/dashboard\/(?:index\.html)?$/.test(pathname) ||
      /\/projects\/agentic-career-boost\/(?:index\.html)?$/.test(pathname);
  }

  async function ensureDashboardScript(pathname = window.location.pathname) {
    if (!needsDashboard(pathname)) return;
    if (window.initProjectDashboard) {
      window.initProjectDashboard();
      return;
    }
    const existing = document.querySelector('script[data-dashboard-runtime="true"]');
    if (existing) {
      await new Promise((resolve) => existing.addEventListener("load", resolve, { once: true }));
      if (window.initProjectDashboard) window.initProjectDashboard();
      return;
    }
    await new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.defer = true;
      script.dataset.dashboardRuntime = "true";
      script.src = assetBase ? new URL("dashboard.js", assetBase).href : "assets/js/dashboard.js";
      script.addEventListener("load", resolve, { once: true });
      script.addEventListener("error", reject, { once: true });
      document.head.appendChild(script);
    });
    if (window.initProjectDashboard) window.initProjectDashboard();
  }

  function syncHead(nextDoc) {
    const selectors = [
      'link[rel="canonical"]',
      'link[rel="manifest"]',
      'link[rel="alternate"][type="application/json"]',
      'meta[name="description"]',
      'meta[property^="og:"]',
      'meta[name^="twitter:"]',
    ];
    selectors.forEach((selector) => {
      document.head.querySelectorAll(selector).forEach((node) => node.remove());
      nextDoc.head.querySelectorAll(selector).forEach((node) => {
        document.head.appendChild(document.importNode(node, true));
      });
    });
  }

  async function softNavigate(url, push = true) {
    document.documentElement.classList.add("is-os-loading");
    try {
      const response = await fetch(url.href, { credentials: "same-origin" });
      if (!response.ok) throw new Error(`Route failed: ${response.status}`);
      const html = await response.text();
      const nextDoc = new DOMParser().parseFromString(html, "text/html");
      const nextRail = nextDoc.querySelector(".os-rail");
      const nextDocument = nextDoc.querySelector(".os-document");
      const nextMeta = nextDoc.querySelector(".os-meta");
      const currentRail = document.querySelector(".os-rail");
      const currentDocument = document.querySelector(".os-document");
      const currentMeta = document.querySelector(".os-meta");
      if (!nextDocument || !currentDocument) throw new Error("Route is not an OS document");

      if (push) window.history.pushState({ osRoute: url.href }, "", url.href);
      document.title = nextDoc.title;
      syncHead(nextDoc);
      syncRuntimeUrls();
      if (nextDoc.body) document.body.className = nextDoc.body.className;
      if (nextRail && currentRail) currentRail.replaceWith(document.importNode(nextRail, true));
      currentDocument.replaceWith(document.importNode(nextDocument, true));
      if (nextMeta && currentMeta) currentMeta.replaceWith(document.importNode(nextMeta, true));
      setTheme(document.documentElement.dataset.theme, false);
      wireThemeToggles();
      wireSignalGalleries();
      wireHoloWindows();
      await hydrateSharedContent(url.href);
      secureExternalLinks();
      await ensureCvScript(url.pathname);
      await ensureDashboardScript(url.pathname);
    } finally {
      document.documentElement.classList.remove("is-os-loading");
    }
  }

  function shouldSoftNavigate(link, event) {
    if (event.defaultPrevented || event.button !== 0) return null;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return null;
    return internalHtmlTarget(link);
  }

  function wireSoftNavigation() {
    if (document.documentElement.dataset.osReady === "nav") return;
    document.documentElement.dataset.osReady = "nav";
    document.addEventListener("click", (event) => {
      const link = event.target.closest?.("a[href]");
      if (!link) return;
      const url = shouldSoftNavigate(link, event);
      if (!url) return;
      event.preventDefault();
      softNavigate(url).catch(() => {
        window.location.href = url.href;
      });
    });
  }

  window.addEventListener("popstate", () => {
    const url = new URL(window.location.href);
    if (isCvPath(url.pathname) && window.initCvView && document.querySelector("[data-cv-view]")) {
      window.initCvView();
      return;
    }
    softNavigate(url, false).catch(() => window.location.reload());
  });

  setTheme(preferredTheme(), false);
  hydrateSharedContent().catch(() => syncRuntimeUrls());
  wireThemeToggles();
  wireSignalGalleries();
  wireHoloWindows();
  secureExternalLinks();
  ensureDashboardScript();
  wireSoftNavigation();
})();
