import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { portfolioRoutes } from "./content-routes.mjs";

const [dist = "site/dist", expectedBase = "/", indexableArg = "false", origin = "https://example.invalid"] = process.argv.slice(2);
const indexable = indexableArg === "true";
const normalizedBase = expectedBase === "/" ? "/" : `/${expectedBase.replace(/^\/+|\/+$/g, "")}/`;
const routes = portfolioRoutes();
const retired = ["/application-tracker/", "/dashboard/", "/hire/", "/hire/ml-ai/", "/hire/agentic/", "/hire/backend/", "/focus/", "/focus/ml-data/", "/focus/agentic/", "/focus/backend/"];

const pageFile = (route) => route === "/" ? join(dist, "index.html") : join(dist, route.replace(/^\//, ""), "index.html");
const htmlFiles = routes.map(pageFile);
const errors = [];
const expectedPrefix = normalizedBase === "/" ? "/" : normalizedBase;
const deploymentLiteral = /["'`](\/AgenticCareerBoost\/)/;

function fail(message) {
  errors.push(message);
}

for (const file of htmlFiles) {
  if (!existsSync(file)) fail(`missing route artifact: ${file}`);
}

for (const route of retired) {
  if (existsSync(pageFile(route))) fail(`retired route still emitted: ${route}`);
}

for (const [route, file] of routes.map((route, index) => [route, htmlFiles[index]])) {
  if (!existsSync(file)) continue;
  const html = readFileSync(file, "utf8");
  const canonicalPath = new URL(html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] ?? "", origin).pathname;
  const expectedCanonicalPath = route;
  if (canonicalPath !== expectedCanonicalPath) fail(`${route}: canonical path ${canonicalPath} != ${expectedCanonicalPath}`);
  if (!html.includes('property="og:title"')) fail(`${route}: missing og:title`);
  if (!html.includes('property="og:description"')) fail(`${route}: missing og:description`);
  if (!html.includes('property="og:image"')) fail(`${route}: missing og:image`);
  if (!html.includes('name="twitter:card"')) fail(`${route}: missing twitter card metadata`);
  const ogImage = html.match(/<meta property="og:image" content="([^"]+)"/)?.[1];
  if (!ogImage) {
    fail(`${route}: missing og:image value`);
  } else {
    const ogPath = new URL(ogImage, origin).pathname;
    if (!ogPath.startsWith(expectedPrefix)) fail(`${route}: og:image ignores deployment base: ${ogPath}`);
  }
  if (indexable && html.includes("noindex,nofollow")) fail(`${route}: canonical build unexpectedly noindex`);
  if (!indexable && !html.includes("noindex,nofollow")) fail(`${route}: mirror build missing noindex`);
  if (deploymentLiteral.test(html) && normalizedBase !== "/AgenticCareerBoost/") fail(`${route}: deployment prefix is hardcoded in generated HTML`);
}

const notFound = join(dist, "404.html");
if (!existsSync(notFound)) {
  fail("missing 404.html");
} else {
  const html = readFileSync(notFound, "utf8");
  if (!html.includes("noindex,nofollow")) fail("404 must be noindex");
}

const robotsFile = join(dist, "robots.txt");
if (!existsSync(robotsFile)) {
  fail("missing robots.txt");
} else {
  const robots = readFileSync(robotsFile, "utf8");
  if (indexable) {
    if (!robots.includes("Allow: /")) fail("indexable build robots.txt must allow crawling");
    if (robots.includes("Disallow: /")) fail("indexable build robots.txt blocks crawling");
    if (!robots.includes(`${origin}/sitemap-index.xml`)) fail("indexable build robots.txt missing sitemap");
  } else if (!robots.includes("Disallow: /")) {
    fail("mirror build robots.txt must block crawling");
  }
}

const sitemap = join(dist, "sitemap-index.xml");
if (indexable && !existsSync(sitemap)) fail("indexable build missing sitemap-index.xml");
if (!indexable && existsSync(sitemap)) fail("mirror build should not emit a sitemap");

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`Verified ${routes.length} generated routes for base ${normalizedBase} (indexable=${indexable}).`);
