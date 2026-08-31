import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import { extname, join, normalize, resolve } from "node:path";
import { chromium } from "playwright";

const output = resolve(process.argv[2] || "site/dist");
const mime = { ".css": "text/css", ".js": "text/javascript", ".html": "text/html", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml", ".webp": "image/webp" };
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
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const errors = [];
const failed = [];
page.on("pageerror", (error) => errors.push(error.message));
page.on("requestfailed", (request) => { if (request.url().startsWith(origin)) failed.push(request.url()); });
for (const route of ["/", "/projects/", "/projects/agentic-career-boost/", "/projects/p3ctex/"]) {
  await page.goto(new URL(route, origin), { waitUntil: "networkidle" });
}
await page.goto(origin, { waitUntil: "networkidle" });
await page.getByRole("link", { name: /Projects/ }).first().click();
if (!page.url().endsWith("/projects/")) throw new Error("Ordinary navigation did not reach projects.");
await page.goto(origin, { waitUntil: "networkidle" });
await page.locator("[data-theme-toggle]").click();
const theme = await page.locator("html").getAttribute("data-theme");
await page.reload({ waitUntil: "networkidle" });
if (await page.locator("html").getAttribute("data-theme") !== theme) throw new Error("Theme did not persist after reload.");
const gallery = page.locator("[data-gallery]");
const before = await gallery.getAttribute("data-slide");
await page.locator("[data-gallery-next]").click();
if (await gallery.getAttribute("data-slide") === before) throw new Error("Gallery next did not change state.");
await page.locator("[data-gallery-expand]").click();
if (await gallery.getAttribute("data-expanded") !== "true") throw new Error("Gallery did not expand.");
for (const viewport of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
  await page.setViewportSize(viewport);
  await page.goto(origin, { waitUntil: "networkidle" });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  if (overflow) throw new Error(`Horizontal overflow at ${viewport.width}px`);
}
await browser.close();
await new Promise((done) => server.close(done));
if (errors.length || failed.length) throw new Error(`Browser errors: ${errors.join(" | ")}; failed same-origin requests: ${failed.join(" | ")}`);
console.log("Browser smoke passed.");
