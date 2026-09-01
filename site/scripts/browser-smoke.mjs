import { createServer } from "node:http";
import { mkdir, readFile, rm, stat } from "node:fs/promises";
import { extname, join, normalize, resolve } from "node:path";
import { chromium } from "playwright";

const output = resolve(process.argv[2] || "site/dist");
const evidenceDir = process.argv[3] ? resolve(process.argv[3]) : null;
if (evidenceDir) {
  await rm(evidenceDir, { recursive: true, force: true });
  await mkdir(evidenceDir, { recursive: true });
}

const mime = { ".css": "text/css", ".js": "text/javascript", ".html": "text/html", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml", ".webp": "image/webp", ".xml": "application/xml", ".txt": "text/plain" };
const server = createServer(async (request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
  const candidate = normalize(join(output, pathname === "/" ? "index.html" : pathname));
  if (!candidate.startsWith(output)) return response.writeHead(403).end();
  const file = candidate.endsWith("/") ? join(candidate, "index.html") : candidate;
  try {
    const info = await stat(file);
    const target = info.isDirectory() ? join(file, "index.html") : file;
    response.writeHead(200, { "content-type": mime[extname(target)] || "application/octet-stream" });
    response.end(await readFile(target));
  } catch { response.writeHead(404).end("not found"); }
});
await new Promise((done) => server.listen(0, "127.0.0.1", done));
const { port } = server.address();
const origin = `http://127.0.0.1:${port}`;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const pageErrors = [];
const consoleErrors = [];
const failedRequests = [];
const badResponses = [];
page.on("pageerror", (error) => pageErrors.push(error.message));
page.on("console", (message) => { if (message.type() === "error") consoleErrors.push(message.text()); });
page.on("requestfailed", (request) => { if (request.url().startsWith(origin)) failedRequests.push(request.url()); });
page.on("response", (response) => { if (response.url().startsWith(origin) && response.status() >= 400) badResponses.push(`${response.status()} ${response.url()}`); });

const routes = [
  "/", "/projects/", "/projects/agentic-career-boost/", "/projects/p3ctex/", "/projects/aaaat/", "/projects/ironbank/",
  "/blog/", "/blog/agents-need-receipts/", "/blog/static-sites-as-workbenches/", "/blog/sprint-review-agenticcareerboost/",
  "/cv/ml/", "/cv/agentic/", "/cv/backend/", "/cv/print/", "/contact/"
];

async function open(route) {
  const response = await page.goto(new URL(route, origin).toString(), { waitUntil: "networkidle" });
  if (!response || response.status() !== 200) throw new Error(`Expected HTTP 200 for ${route}, got ${response?.status() ?? "no response"}`);
}

async function assertDecodedImages(route) {
  const images = page.locator("img");
  for (let index = 0; index < await images.count(); index += 1) {
    const image = images.nth(index);
    await image.scrollIntoViewIfNeeded();
    try { await image.evaluate((node) => node.decode()); } catch {}
    const state = await image.evaluate((node) => ({ src: node.currentSrc || node.src, complete: node.complete, width: node.naturalWidth, height: node.naturalHeight }));
    if (!state.complete || state.width <= 0 || state.height <= 0) throw new Error(`Image did not decode on ${route}: ${state.src}`);
  }
}

async function assertShell(route, viewportWidth) {
  const avatarSrc = await page.locator(".identity-avatar img").getAttribute("src");
  if (!avatarSrc?.endsWith("/img/avatar.jpg")) throw new Error(`Identity avatar is not avatar.jpg on ${route}: ${avatarSrc}`);
  const favicon = await page.locator('link[rel="icon"]').getAttribute("href");
  if (!favicon?.endsWith("/img/avatar.jpg")) throw new Error(`Browser icon is not avatar.jpg on ${route}: ${favicon}`);
  const faviconStatus = await page.evaluate(async (href) => (await fetch(href)).status, favicon);
  if (faviconStatus !== 200) throw new Error(`Browser icon failed to load on ${route}: HTTP ${faviconStatus}`);

  const tabs = page.locator(".primary-nav--tabs a");
  if (await tabs.count() !== 5) throw new Error(`Expected five shared navigation tabs on ${route}`);
  const tabTops = await tabs.evaluateAll((nodes) => [...new Set(nodes.map((node) => Math.round(node.getBoundingClientRect().top)))]);
  if (tabTops.length !== 1) throw new Error(`Shared navigation wrapped on ${route} at ${viewportWidth}px`);
  if (await page.locator(".primary-nav--tabs a.is-active").count() !== 1) throw new Error(`Shared navigation must have exactly one active tab on ${route}`);

  const bannerHeight = await page.locator(".site-banner").evaluate((node) => node.getBoundingClientRect().height);
  if (bannerHeight < 100) throw new Error(`Banner is too shallow on ${route} at ${viewportWidth}px: ${bannerHeight}px`);

  const railDisplay = await page.locator(".primary-nav--rail").evaluate((node) => getComputedStyle(node).display);
  if (viewportWidth <= 832 && railDisplay !== "none") throw new Error(`Rail navigation should not duplicate tabs at ${viewportWidth}px`);
  if (viewportWidth > 832 && railDisplay === "none") throw new Error(`Rail navigation unexpectedly hidden at ${viewportWidth}px`);
}

async function setTheme(theme) {
  await page.evaluate((nextTheme) => {
    const key = document.documentElement.dataset.themeStorageKey;
    if (key) localStorage.setItem(key, nextTheme);
  }, theme);
  await page.reload({ waitUntil: "networkidle" });
}

async function capture(name, fullPage = true) {
  if (!evidenceDir) return;
  await page.screenshot({ path: join(evidenceDir, `${name}.png`), fullPage, animations: "disabled" });
}

for (const route of routes) await open(route);

await open("/");
await assertDecodedImages("/");
await assertShell("/", 1920);
if (!(await page.locator(".primary-nav--tabs a.is-active").textContent())?.includes("Home")) throw new Error("Home tab is not active on Home.");
await page.evaluate(() => {
  window.__acbClientNavigationMarker = "alive";
  const banner = document.querySelector(".site-banner");
  const avatar = document.querySelector(".identity-avatar");
  if (!banner || !avatar) throw new Error("Persistent shell elements are missing on Home.");
  banner.dataset.persistenceProbe = "banner";
  avatar.dataset.persistenceProbe = "avatar";
});
await page.locator('.primary-nav--tabs a[href$="/projects/"]').click();
await page.waitForURL(new URL("/projects/", origin).toString());
await page.locator("main").waitFor();
const projectNavigation = await page.evaluate(() => ({
  marker: window.__acbClientNavigationMarker,
  banner: document.querySelector(".site-banner")?.dataset.persistenceProbe,
  avatar: document.querySelector(".identity-avatar")?.dataset.persistenceProbe
}));
if (projectNavigation.marker !== "alive") throw new Error("Internal navigation performed a full document reload.");
if (projectNavigation.banner !== "banner" || projectNavigation.avatar !== "avatar") throw new Error("Shared banner/avatar DOM was replaced during internal navigation.");
if (!(await page.locator(".primary-nav--tabs a.is-active").textContent())?.includes("Projects")) throw new Error("Projects tab did not become active after client navigation.");

await page.locator('.primary-nav--tabs a[href$="/"]').first().click();
await page.waitForURL(new URL("/", origin).toString());
await page.locator("[data-monitor]").waitFor();
if (await page.evaluate(() => window.__acbClientNavigationMarker) !== "alive") throw new Error("Client navigation context was lost when returning Home.");

const monitor = page.locator("[data-monitor]");
const image = page.locator("[data-monitor-image]");
const before = { src: await image.getAttribute("src"), title: await page.locator("[data-monitor-title]").textContent(), position: await page.locator("[data-monitor-position]").textContent() };
await page.locator("[data-monitor-next]").click();
try { await image.evaluate((node) => node.decode()); } catch {}
const after = { src: await image.getAttribute("src"), title: await page.locator("[data-monitor-title]").textContent(), position: await page.locator("[data-monitor-position]").textContent(), width: await image.evaluate((node) => node.naturalWidth) };
if (after.src === before.src || after.title === before.title || after.position === before.position || after.width <= 0) throw new Error("Monitor next did not load a distinct, decoded project signal after client navigation.");
await page.locator("[data-monitor-prev]").click();
if (await image.getAttribute("src") !== before.src || await page.locator("[data-monitor-title]").textContent() !== before.title) throw new Error("Monitor previous did not restore the original project signal.");
await page.locator("[data-monitor-expand]").click();
if (await monitor.getAttribute("data-expanded") !== "true" || await monitor.getAttribute("role") !== "dialog" || await monitor.getAttribute("aria-modal") !== "true") throw new Error("Monitor expansion state is incomplete.");
if (!await page.locator("body").evaluate((node) => node.classList.contains("monitor-open"))) throw new Error("Expanded monitor did not lock the page state.");
await page.keyboard.press("Escape");
if (await monitor.getAttribute("data-expanded") !== "false" || await monitor.getAttribute("aria-modal") !== null) throw new Error("Escape did not close the monitor cleanly.");

await page.locator("[data-theme-toggle]").click();
const theme = await page.locator("html").getAttribute("data-theme");
await page.reload({ waitUntil: "networkidle" });
if (await page.locator("html").getAttribute("data-theme") !== theme) throw new Error("Theme did not persist after reload.");

const viewports = [
  { width: 1920, height: 1080, name: "desktop-1920" },
  { width: 1366, height: 768, name: "desktop-1366" },
  { width: 768, height: 1024, name: "tablet-768" },
  { width: 390, height: 844, name: "mobile-390" }
];
const responsiveRoutes = ["/", "/projects/", "/projects/agentic-career-boost/", "/cv/ml/", "/blog/", "/contact/", "/blog/agents-need-receipts/"];
const evidenceRoutes = new Map([["/", "home"], ["/projects/agentic-career-boost/", "project-acb"], ["/cv/ml/", "cv-ml"], ["/blog/", "blog"], ["/contact/", "contact"]]);

for (const viewport of viewports) {
  await page.setViewportSize(viewport);
  for (const route of responsiveRoutes) {
    await open(route);
    await assertShell(route, viewport.width);
    if (["/", "/projects/agentic-career-boost/", "/cv/ml/", "/blog/", "/contact/"].includes(route)) await assertDecodedImages(route);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    if (overflow > 1) {
      const offenders = await page.evaluate(() => [...document.querySelectorAll("body *")]
        .filter((node) => node.getBoundingClientRect().right > window.innerWidth + 1 || node.getBoundingClientRect().left < -1)
        .slice(0, 5)
        .map((node) => `${node.tagName.toLowerCase()}.${[...node.classList].join(".")}`));
      throw new Error(`Horizontal overflow ${overflow}px at ${viewport.width}px on ${route}; offenders: ${offenders.join(", ")}`);
    }
    if (evidenceRoutes.has(route)) {
      await setTheme("light");
      await assertDecodedImages(route);
      await capture(`${viewport.name}-${evidenceRoutes.get(route)}-light`);
      if (viewport.width === 1920 && route === "/") {
        await page.locator("[data-monitor-expand]").click();
        if (await monitor.getAttribute("data-expanded") !== "true") throw new Error("Monitor did not expand for visual evidence.");
        await capture(`${viewport.name}-home-monitor-expanded-light`, false);
        await page.keyboard.press("Escape");
        if (await monitor.getAttribute("data-expanded") !== "false") throw new Error("Monitor did not close after visual evidence.");
        await setTheme("dark");
        await assertDecodedImages(route);
        await capture(`${viewport.name}-home-dark`);
      }
    }
  }
}

const noJsContext = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
const noJsPage = await noJsContext.newPage();
for (const route of ["/", "/projects/agentic-career-boost/"]) {
  const response = await noJsPage.goto(new URL(route, origin).toString(), { waitUntil: "load" });
  if (!response || response.status() !== 200) throw new Error(`No-JS route failed: ${route}`);
  if (!(await noJsPage.locator("main").textContent())?.trim()) throw new Error(`No-JS route has no authored content: ${route}`);
}
await noJsContext.close();

await browser.close();
await new Promise((done) => server.close(done));
if (pageErrors.length || consoleErrors.length || failedRequests.length || badResponses.length) throw new Error(`Browser errors: ${pageErrors.join(" | ")}; console: ${consoleErrors.join(" | ")}; failed requests: ${failedRequests.join(" | ")}; bad responses: ${badResponses.join(" | ")}`);
console.log("Browser smoke passed: routes, avatar/favicon, shared tab navigation, client navigation with persisted shell, theme, monitor, responsive layouts at 1920/1366/768/390 and no-JS content.");
