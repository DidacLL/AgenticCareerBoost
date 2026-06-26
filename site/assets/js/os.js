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
      button.textContent = nextTheme === "dark" ? "light mode" : "dark mode";
      button.setAttribute("aria-pressed", String(nextTheme === "dark"));
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
      button.textContent = current === "dark" ? "light mode" : "dark mode";
      button.setAttribute("aria-pressed", String(current === "dark"));
    });
  }

  function secureExternalLinks(root = document) {
    root.querySelectorAll('a[href^="http://"], a[href^="https://"]').forEach((link) => {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    });
  }

  const gallerySlides = [
    {
      label: "portrait.feed",
      image: "assets/img/me.png",
      alt: "Dídac Llorens portrait rendered as a retro monitor feed",
      title: "Dídac Llorens",
      copy: "Software Engineering · UOC<br>ML/Data · Backend · Tooling<br>Barcelona · source-first profile<br>Former banking and insurance operations",
      href: "contact/index.html",
      caption: "portrait / default signal",
      project: false,
    },
    {
      label: "projects.shortcut",
      image: "assets/img/routing-map.png",
      alt: "Routing map preview for selected projects",
      title: "Projects",
      copy: "AgenticCareerBoost · P3CTeX · IronBank<br>Human explanations with source links<br>Start here for the technical map.",
      href: "projects/index.html",
      caption: "shortcut / projects",
      project: true,
    },
    {
      label: "cv.web",
      image: "assets/img/screenshot001.png",
      alt: "CV artifact preview",
      title: "Web CV",
      copy: "Role views · print · PDF export<br>ML/Data · agentic workflow · backend<br>Current professional curriculum.",
      href: "curriculum/index.html?view=ml",
      caption: "shortcut / web CV",
      project: true,
    },
    {
      label: "blog.queue",
      image: "assets/img/sprint-paircheck-loop.png",
      alt: "Blog and review loop preview",
      title: "Blog queue",
      copy: "Future article index and LinkedIn mirrors<br>Project logs · technical decisions · tooling notes<br>Kept source-backed, not fake-filled.",
      href: "blog/index.html",
      caption: "shortcut / blog",
      project: true,
    },
  ];

  function applyGallerySlide(windowNode, index) {
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

  function syncRailState(nextDoc) {
    const nextActive = nextDoc.querySelector(".os-nav a.is-active");
    const currentLinks = document.querySelectorAll(".os-nav a");
    currentLinks.forEach((link) => {
      const isActive = nextActive && link.textContent.trim() === nextActive.textContent.trim();
      link.classList.toggle("is-active", Boolean(isActive));
      if (isActive) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
    });
  }

  async function ensureCvScript() {
    if (!/\/curriculum\//.test(window.location.pathname)) return;
    if (window.initCvView) {
      window.initCvView();
      return;
    }
    if (document.querySelector('script[data-cv-runtime="true"]')) return;
    const script = document.createElement("script");
    script.defer = true;
    script.dataset.cvRuntime = "true";
    script.src = assetBase ? new URL("cv.js", assetBase).href : "assets/js/cv.js";
    document.head.appendChild(script);
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
    const response = await fetch(url.href, { credentials: "same-origin" });
    if (!response.ok) throw new Error(`Route failed: ${response.status}`);
    const html = await response.text();
    const nextDoc = new DOMParser().parseFromString(html, "text/html");
    const nextDocument = nextDoc.querySelector(".os-document");
    const nextMeta = nextDoc.querySelector(".os-meta");
    const currentDocument = document.querySelector(".os-document");
    const currentMeta = document.querySelector(".os-meta");
    if (!nextDocument || !currentDocument) throw new Error("Route is not an OS document");

    if (push) window.history.pushState({ osRoute: url.href }, "", url.href);
    document.title = nextDoc.title;
    syncHead(nextDoc);
    syncRailState(nextDoc);
    currentDocument.replaceWith(document.importNode(nextDocument, true));
    if (nextMeta && currentMeta) currentMeta.replaceWith(document.importNode(nextMeta, true));
    setTheme(document.documentElement.dataset.theme, false);
    wireThemeToggles();
    wireSignalGalleries();
    wireHoloWindows();
    secureExternalLinks();
    wireSoftNavigation();
    await ensureCvScript();
    document.documentElement.classList.remove("is-os-loading");
  }

  function wireSoftNavigation(root = document) {
    root.querySelectorAll(".os-nav a, .doc-tabs a, .preview-row, .mini-monitor, .file-list a").forEach((link) => {
      if (link.dataset.osReady === "nav") return;
      link.dataset.osReady = "nav";
      link.addEventListener("click", (event) => {
        const url = internalHtmlTarget(link);
        if (!url) return;
        event.preventDefault();
    softNavigate(url).catch(() => {
      window.location.href = url.href;
    });
      });
    });
  }

  window.addEventListener("popstate", () => {
    const url = new URL(window.location.href);
    softNavigate(url, false).catch(() => window.location.reload());
  });

  setTheme(preferredTheme(), false);
  wireThemeToggles();
  wireSignalGalleries();
  wireHoloWindows();
  secureExternalLinks();
  wireSoftNavigation();
})();
