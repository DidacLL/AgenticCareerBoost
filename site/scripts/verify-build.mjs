import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

const [outputArg, baseArg = "/", indexableArg = "false", originArg = "https://example.invalid"] = process.argv.slice(2);
if (!outputArg) throw new Error("Usage: node verify-build.mjs <dist> [base] [indexable] [origin]");
const output = resolve(outputArg);
const base = baseArg === "/" ? "/" : `/${baseArg.replace(/^\/+|\/+$/g, "")}/`;
const indexable = indexableArg === "true";
const origin = new URL(originArg);
const routes = [
  "/", "/projects/", "/projects/agentic-career-boost/", "/projects/p3ctex/", "/projects/aaaat/", "/projects/ironbank/",
  "/blog/", "/blog/agents-need-receipts/", "/blog/static-sites-as-workbenches/", "/blog/sprint-review-agenticcareerboost/",
  "/cv/ml/", "/cv/agentic/", "/cv/backend/", "/cv/print/", "/contact/"
];
const retired = [
  "/dashboard/", "/application-tracker/", "/curriculum/", "/notes/", "/hire/", "/hire/ml/", "/hire/agentic/", "/hire/backend/",
  "/focus/", "/focus/ml/", "/focus/agentic/", "/focus/backend/"
];
const walk = (dir) => readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
  const path = join(dir, entry.name);
  return entry.isDirectory() ? walk(path) : [path];
});

for (const file of walk(resolve("site/src"))) {
  const source = readFileSync(file, "utf8");
  const ownOrigin = /https?:\/\/didacll\.github\.io/i.test(source);
  const hardcodedProjectBase = /["'`]\/AgenticCareerBoost\//.test(source);
  if (ownOrigin || hardcodedProjectBase) throw new Error(`Own host or deployment prefix found in site source: ${file}`);
}

const pageFile = (route) => join(output, route === "/" ? "index.html" : route.replace(/^\//, "") + "index.html");
const refs = (html) => [...html.matchAll(/(?:href|src)=[\"']([^\"'#]+)[\"']/gi)].map((match) => match[1]);
const canonicalHref = (html) => html.match(/<link\s+rel=[\"']canonical[\"']\s+href=[\"']([^\"']+)[\"']/i)?.[1];
const hasNoindex = (html) => /<meta\s+name=[\"']robots[\"']\s+content=[\"'][^\"']*noindex/i.test(html);

for (const route of routes) {
  const file = pageFile(route);
  if (!existsSync(file)) throw new Error(`Missing generated route: ${route}`);
  const html = readFileSync(file, "utf8");
  for (const required of [/<title>[^<]+<\/title>/i, /<meta name="description"/i, /<link rel="canonical"/i, /<main[ >]/i]) {
    if (!required.test(html)) throw new Error(`Missing page metadata or main region: ${route}`);
  }
  const canonical = canonicalHref(html);
  const expectedCanonical = new URL(route, origin).toString();
  if (canonical !== expectedCanonical) throw new Error(`Canonical mismatch on ${route}: expected ${expectedCanonical}, got ${canonical ?? "missing"}`);
  if (indexable === hasNoindex(html)) throw new Error(`Robots metadata mismatch on ${route}: indexable=${indexable}`);
  for (const reference of refs(html)) {
    if (/^(?:https?:|mailto:|tel:|data:|#)/i.test(reference) || /\/files\/cv\//.test(reference)) continue;
    const clean = reference.split(/[?#]/, 1)[0];
    const local = clean.startsWith("/") ? clean.replace(base, "/").replace(/^\//, "") : clean;
    const resolved = join(output, local || "index.html");
    if (!existsSync(resolved) && !existsSync(join(resolved, "index.html"))) throw new Error(`Broken generated reference ${reference} from ${route}`);
  }
}

for (const route of retired) {
  if (existsSync(pageFile(route))) throw new Error(`Retired route was regenerated: ${route}`);
}

const notFound = join(output, "404.html");
if (!existsSync(notFound)) throw new Error("Missing 404.html");
const notFoundHtml = readFileSync(notFound, "utf8");
if (!/<main[ >]/i.test(notFoundHtml) || !hasNoindex(notFoundHtml)) throw new Error("404 page must render the site shell and remain noindex.");

const robotsFile = join(output, "robots.txt");
if (!existsSync(robotsFile)) throw new Error("Missing robots.txt");
const robots = readFileSync(robotsFile, "utf8");
const sitemapFile = join(output, "sitemap-index.xml");
if (indexable) {
  if (!/Allow:\s*\//i.test(robots) || /Disallow:\s*\//i.test(robots)) throw new Error("Indexable build robots.txt must allow crawling.");
  const expectedSitemap = new URL("/sitemap-index.xml", origin).toString();
  if (!robots.includes(`Sitemap: ${expectedSitemap}`)) throw new Error(`robots.txt missing sitemap ${expectedSitemap}`);
  if (!existsSync(sitemapFile)) throw new Error("Indexable build must contain sitemap-index.xml");
} else {
  if (!/Disallow:\s*\//i.test(robots)) throw new Error("Non-indexable build robots.txt must disallow crawling.");
  if (existsSync(sitemapFile)) throw new Error("Non-indexable mirror must not publish a sitemap.");
}

console.log(`Verified ${routes.length} portfolio routes, metadata/indexability, retired-route absence and base ${base}`);
