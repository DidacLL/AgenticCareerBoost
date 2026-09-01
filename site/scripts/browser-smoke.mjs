import { createReadStream, existsSync, mkdirSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, normalize } from "node:path";
import { chromium } from "playwright";
import { portfolioRoutes, retiredRoutes } from "./content-routes.mjs";

const [dist = "site/dist", evidenceDir = "site/browser-evidence"] = process.argv.slice(2);
const routes = portfolioRoutes();
const responsiveRoutes = ["/", "/projects/agentic-career-boost/", "/blog/", "/cv/ml/", "/contact/"];
const evidenceRoutes = ["/", "/projects/agentic-career-boost/", "/blog/", "/cv/ml/", "/contact/"];
const viewports = [
  { name: "desktop-1920", width: 1920, height: 1080 },
  { name: "desktop-1366", width: 1366, height: 768 },
  { name: "tablet-768", width: 768, height: 1024 },
  { name: "mobile-390", width: 390, height: 844 }
];
const mime = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml", ".pdf": "application/pdf", ".txt": "text/plain", ".xml": "application/xml" };

mkdirSync(evidenceDir, { recursive: true });

function resolveFile(urlPath) {
  const decoded = decodeURIComponent(urlPath.split("?")[0]);
  const safe = normalize(decoded).replace(/^(\.\.(\/|\\|$))+/, "").replace(/^[/\\]+/, "");
  const requested = join(dist, safe);
  if (existsSync(requested) && extname(requested)) return requested;
  const index = join(requested, "index.html");
  if (existsSync(index)) return index;
  const html = `${requested}.html`;
  if (existsSync(html)) return html;
  return join(dist, "404.html");
}

const server = createServer((req, res) => {
  const file = resolveFile(req.url ?? "/");
  const is404 = file.endsWith("404.html") && !["/404.html", "/404"].includes((req.url ?? "").split("?")[0]);
  res.writeHead(is404 ? 404 : 200, { "content-type": mime[extname(file)] ?? "application/octet-stream" });
  createReadStream(file).pipe(res);
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const port = server.address().port;
const origin = `http://127.0.0.1:${port}`;

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const browserErrors = [];
const failedResponses = [];
page.on("pageerror", (error) => browserErrors.push(error.message));
page.on("response", (response) => {
  const url = new URL(response.url());
  if (url.origin === origin && response.status() >= 400) failedResponses.push(`${response.status()} ${url.pathname}`);
});

async function assertImagesDecoded(currentPage, route) {
  const broken = await currentPage.locator("img").evaluateAll((images) => images
    .filter((image) => !image.complete || image.naturalWidth === 0)
    .map((image) => image.getAttribute("src")));
  if (broken.length) throw new Error(`${route}: undecoded images: ${broken.join(", ")}`);
}

for (const route of routes) {
  const response = await page.goto(`${origin}${route}`, { waitUntil: "networkidle" });
  if (!response || response.status() !== 200) throw new Error(`${route}: expected HTTP 200, got ${response?.status()}`);
  await assertImagesDecoded(page, route);
}

for (const route of retiredRoutes) {
  const response = await page.goto(`${origin}${route}`, { waitUntil: "networkidle" });
  if (!response || response.status() !== 404) throw new Error(`${route}: retired route must return HTTP 404`);
}

await page.goto(origin, { waitUntil: "networkidle" });
const faviconHref = await page.locator('link[rel="icon"]').getAttribute("href");
if (!faviconHref || !faviconHref.includes("/img/avatar.jpg")) throw new Error("Browser favicon must use the canonical avatar image");
const faviconResponse = await page.request.get(new URL(faviconHref, origin).toString());
if (faviconResponse.status() !== 200) throw new Error(`Avatar favicon returned HTTP ${faviconResponse.status()}`);
const avatarSrc = await page.locator(".identity-avatar img").getAttribute("src");
if (!avatarSrc || !avatarSrc.includes("/img/avatar.jpg")) throw new Error("Identity rail must use avatar.jpg, not the CRT portrait");

await page.evaluate(() => { window.__navigationContext = "persisted"; });
const bannerBefore = await page.locator(".site-banner").evaluate((node) => { node.dataset.persistenceProbe = "banner"; return node; });
const avatarBefore = await page.locator(".identity-avatar").evaluate((node) => { node.dataset.persistenceProbe = "avatar"; return node; });
void bannerBefore;
void avatarBefore;
await page.locator('.primary-nav--tabs a[href="/projects/"]').click();
await page.waitForURL(`${origin}/projects/`);
if (await page.evaluate(() => window.__navigationContext) !== "persisted") throw new Error("Internal navigation performed a full document reload");
if (await page.locator(".site-banner").getAttribute("data-persistence-probe") !== "banner") throw new Error("Banner node was replaced during client navigation");
if (await page.locator(".identity-avatar").getAttribute("data-persistence-probe") !== "avatar") throw new Error("Avatar node was replaced during client navigation");
const projectsActiveHref = await page.locator('.primary-nav--tabs a[aria-current="page"]').getAttribute("href");
if (new URL(projectsActiveHref ?? "", origin).pathname !== "/projects/") throw new Error("Projects tab did not become active after client navigation");
await page.locator('.primary-nav--tabs a[href="/"]').click();
await page.waitForURL(`${origin}/`);
const homeActiveHref = await page.locator('.primary-nav--tabs a[aria-current="page"]').getAttribute("href");
if (new URL(homeActiveHref ?? "", origin).pathname !== "/") throw new Error("Home tab did not become active after returning through client navigation");

const themeButton = page.locator("[data-theme-toggle]");
const beforeTheme = await page.locator("html").getAttribute("data-theme");
await themeButton.click();
const afterTheme = await page.locator("html").getAttribute("data-theme");
if (!beforeTheme || beforeTheme === afterTheme) throw new Error("Theme toggle did not change theme");
await page.reload({ waitUntil: "networkidle" });
if (await page.locator("html").getAttribute("data-theme") !== afterTheme) throw new Error("Theme preference did not persist after reload");

const monitor = page.locator("[data-monitor]");
if (!await monitor.count()) throw new Error("Home monitor missing after client navigation");
const firstImage = await monitor.locator("[data-monitor-image]").getAttribute("src");
await monitor.locator("[data-monitor-next]").click();
const nextImage = await monitor.locator("[data-monitor-image]").getAttribute("src");
if (!firstImage || firstImage === nextImage) throw new Error("Monitor next control did not advance signal");
await monitor.locator("[data-monitor-expand]").click();
if (await monitor.getAttribute("data-expanded") !== "true") throw new Error("Monitor expand control did not expand");
const expandedBox = await monitor.boundingBox();
if (!expandedBox || expandedBox.width > 1100 || expandedBox.width < 700) throw new Error(`Expanded CRT width is unreasonable at 1920px: ${expandedBox?.width}`);
await page.screenshot({ path: join(evidenceDir, "home-expanded-1920.png"), fullPage: true });
await monitor.locator("[data-monitor-expand]").click();
if (await monitor.getAttribute("data-expanded") !== "false") throw new Error("Monitor expand control did not collapse");

for (const viewport of viewports) {
  await page.setViewportSize({ width: viewport.width, height: viewport.height });
  for (const route of responsiveRoutes) {
    failedResponses.length = 0;
    const response = await page.goto(`${origin}${route}`, { waitUntil: "networkidle" });
    if (!response || response.status() !== 200) throw new Error(`${route}@${viewport.name}: expected HTTP 200`);
    await assertImagesDecoded(page, `${route}@${viewport.name}`);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    if (overflow > 1) throw new Error(`${route}@${viewport.name}: horizontal overflow ${overflow}px`);
    const tabs = page.locator(".primary-nav--tabs a");
    if (await tabs.count() !== 5) throw new Error(`${route}@${viewport.name}: expected five primary tabs`);
    const tabRows = await tabs.evaluateAll((nodes) => new Set(nodes.map((node) => Math.round(node.getBoundingClientRect().top))).size);
    if (tabRows !== 1) throw new Error(`${route}@${viewport.name}: primary tabs wrapped onto ${tabRows} rows`);
    if (await page.locator('.primary-nav--tabs a[aria-current="page"]').count() !== 1) throw new Error(`${route}@${viewport.name}: expected one active primary tab`);
    const bannerHeight = await page.locator(".site-banner").evaluate((node) => node.getBoundingClientRect().height);
    if (bannerHeight < 100) throw new Error(`${route}@${viewport.name}: banner is too thin (${bannerHeight}px)`);
    if (viewport.width <= 768) {
      const railDisplay = await page.locator(".primary-nav--rail").evaluate((node) => getComputedStyle(node).display);
      if (railDisplay !== "none") throw new Error(`${route}@${viewport.name}: duplicate rail navigation should be hidden in vertical layouts`);
    }
  }
}

await page.setViewportSize({ width: 1920, height: 1080 });
for (const route of evidenceRoutes) {
  await page.goto(`${origin}${route}`, { waitUntil: "networkidle" });
  const name = route === "/" ? "home" : route.replace(/^\/|\/$/g, "").replaceAll("/", "-");
  await page.screenshot({ path: join(evidenceDir, `${name}-1920.png`), fullPage: true });
}
await page.goto(origin, { waitUntil: "networkidle" });
await page.locator("[data-theme-toggle]").click();
await page.screenshot({ path: join(evidenceDir, "home-dark-1920.png"), fullPage: true });

const noJs = await browser.newPage({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
const noJsResponse = await noJs.goto(origin, { waitUntil: "load" });
if (!noJsResponse || noJsResponse.status() !== 200) throw new Error("No-JS Home did not load");
if (!await noJs.locator("main").count()) throw new Error("No-JS Home missing main content");
await assertImagesDecoded(noJs, "no-js-home");
await noJs.close();

if (browserErrors.length) throw new Error(`Browser errors:\n${browserErrors.join("\n")}`);
if (failedResponses.length) throw new Error(`Same-origin HTTP failures:\n${failedResponses.join("\n")}`);

await browser.close();
await new Promise((resolve) => server.close(resolve));
console.log(`Browser smoke passed for ${routes.length} discovered routes across ${viewports.length} viewport profiles.`);
