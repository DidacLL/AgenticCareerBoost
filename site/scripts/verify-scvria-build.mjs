import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { extname, join, relative, sep } from "node:path";

const [dist = "site/dist-scvria", productsDir = "site/scvria/src/content/products"] = process.argv.slice(2);
const requiredRoutes = ["/", "/software/", "/manifesto/", "/community/", "/about/"];
const errors = [];

function fail(message) {
  errors.push(message);
}

function pageFile(route) {
  return route === "/" ? join(dist, "index.html") : join(dist, route.replace(/^\/+|\/+$/g, ""), "index.html");
}

function walkFiles(root) {
  if (!existsSync(root)) return [];
  const files = [];

  for (const entry of readdirSync(root, { withFileTypes: true })) {
    const path = join(root, entry.name);
    if (entry.isDirectory()) files.push(...walkFiles(path));
    else if (entry.isFile()) files.push(path);
  }

  return files;
}

function productIds() {
  return walkFiles(productsDir)
    .filter((file) => extname(file).toLowerCase() === ".md")
    .map((file) => relative(productsDir, file).slice(0, -3).split(sep).join("/"))
    .sort();
}

function generatedProductIds() {
  const softwareDir = join(dist, "software");
  if (!existsSync(softwareDir)) return [];

  return walkFiles(softwareDir)
    .filter((file) => file.endsWith(`${sep}index.html`) && file !== join(softwareDir, "index.html"))
    .map((file) => relative(softwareDir, file).split(sep).slice(0, -1).join("/"))
    .sort();
}

function attributes(tag) {
  const attrs = new Map();
  const pattern = /([:\w-]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/g;

  for (const match of tag.matchAll(pattern)) {
    attrs.set(match[1].toLowerCase(), match[2] ?? match[3] ?? match[4] ?? "");
  }

  return attrs;
}

function textContent(value) {
  return value.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
}

function artifactForPath(pathname) {
  if (pathname === "/") return join(dist, "index.html");
  const clean = pathname.replace(/^\/+/, "");
  if (pathname.endsWith("/")) return join(dist, clean, "index.html");

  const direct = join(dist, clean);
  if (existsSync(direct) && statSync(direct).isFile()) return direct;
  return join(dist, clean, "index.html");
}

function verifyInternalLinks(route, html) {
  const base = new URL(route, "https://scvria.invalid");

  for (const match of html.matchAll(/<a\b[^>]*\bhref\s*=\s*(?:"([^"]*)"|'([^']*)')/gi)) {
    const href = (match[1] ?? match[2] ?? "").replace(/&amp;/g, "&").trim();
    if (!href || href.startsWith("#") || /^(?:mailto:|tel:|javascript:)/i.test(href)) continue;

    let target;
    try {
      target = new URL(href, base);
    } catch {
      fail(`${route}: invalid link href ${JSON.stringify(href)}`);
      continue;
    }

    if (target.origin !== base.origin) continue;

    const file = artifactForPath(target.pathname);
    if (!existsSync(file)) fail(`${route}: internal link ${href} does not resolve to generated output (${file})`);
  }
}

const expectedProductIds = productIds();
const expectedProductRoutes = expectedProductIds.map((id) => `/software/${id}/`);
const routes = [...requiredRoutes, ...expectedProductRoutes];

for (const route of routes) {
  const file = pageFile(route);
  if (!existsSync(file)) {
    fail(`missing route artifact: ${route} -> ${file}`);
    continue;
  }

  const html = readFileSync(file, "utf8");
  if (!html.trim()) {
    fail(`${route}: generated HTML is empty`);
    continue;
  }

  const title = textContent(html.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i)?.[1] ?? "");
  if (!title) fail(`${route}: missing or empty <title>`);

  const description = [...html.matchAll(/<meta\b[^>]*>/gi)]
    .map((match) => attributes(match[0]))
    .find((attrs) => attrs.get("name")?.toLowerCase() === "description")
    ?.get("content")
    ?.trim();
  if (!description) fail(`${route}: missing or empty meta description`);

  if (!html.includes("SCVRIA Sofware")) fail(`${route}: missing intentional 'SCVRIA Sofware' brand spelling`);
  if (html.includes("SCVRIA Software")) fail(`${route}: contains incorrect 'SCVRIA Software' spelling`);

  verifyInternalLinks(route, html);
}

const actualProductIds = generatedProductIds();
for (const id of actualProductIds) {
  if (!expectedProductIds.includes(id)) fail(`/software/${id}/: generated product page has no matching Markdown product entry`);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

const catalog = expectedProductIds.length === 0
  ? "empty product catalog accepted"
  : `${expectedProductIds.length} product route${expectedProductIds.length === 1 ? "" : "s"} verified`;
console.log(`Verified ${requiredRoutes.length} required SCVRIA routes; ${catalog}; internal links resolve.`);
