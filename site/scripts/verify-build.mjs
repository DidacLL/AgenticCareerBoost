import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

const [outputArg, baseArg = "/"] = process.argv.slice(2);
if (!outputArg) throw new Error("Usage: node verify-build.mjs <dist> [base]");
const output = resolve(outputArg);
const base = baseArg === "/" ? "/" : `/${baseArg.replace(/^\/+|\/+$/g, "")}/`;
const routes = [
  "/", "/projects/", "/projects/agentic-career-boost/", "/projects/p3ctex/", "/projects/aaaat/", "/projects/ironbank/",
  "/blog/", "/blog/agents-need-receipts/", "/blog/static-sites-as-workbenches/", "/blog/sprint-review-agenticcareerboost/",
  "/cv/ml/", "/cv/agentic/", "/cv/backend/", "/cv/print/",
  "/focus/", "/focus/ml/", "/focus/agentic/", "/focus/backend/", "/contact/"
];
const retired = ["/dashboard/", "/application-tracker/", "/curriculum/", "/notes/", "/hire/", "/hire/ml/", "/hire/agentic/", "/hire/backend/"];
const walk = (dir) => readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
  const path = join(dir, entry.name);
  return entry.isDirectory() ? walk(path) : [path];
});

for (const file of walk(resolve("site/src"))) {
  const source = readFileSync(file, "utf8");
  const ownOrigin = /https?:\/\/didacll\.github\.io/i.test(source);
  const hardcodedProjectBase = /["'`]\/AgenticCareerBoost\//.test(source);
  if (ownOrigin || hardcodedProjectBase) {
    throw new Error(`Own host or deployment prefix found in site source: ${file}`);
  }
}

const pageFile = (route) => join(output, route === "/" ? "index.html" : route.replace(/^\//, "") + "index.html");
const refs = (html) => [...html.matchAll(/(?:href|src)=[\"']([^\"'#]+)[\"']/gi)].map((match) => match[1]);
for (const route of routes) {
  const file = pageFile(route);
  if (!existsSync(file)) throw new Error(`Missing generated route: ${route}`);
  const html = readFileSync(file, "utf8");
  for (const required of [/<title>[^<]+<\/title>/i, /<meta name="description"/i, /<link rel="canonical"/i, /<main[ >]/i]) {
    if (!required.test(html)) throw new Error(`Missing page metadata or main region: ${route}`);
  }
  for (const reference of refs(html)) {
    if (/^(?:https?:|mailto:|tel:|data:|#)/i.test(reference) || /\/files\/cv\//.test(reference)) continue;
    const clean = reference.split(/[?#]/, 1)[0];
    const local = clean.startsWith("/") ? clean.replace(base, "/").replace(/^\//, "") : clean;
    const resolved = join(output, local || "index.html");
    if (!existsSync(resolved) && !existsSync(join(resolved, "index.html"))) {
      throw new Error(`Broken generated reference ${reference} from ${route}`);
    }
  }
}
for (const route of retired) {
  if (existsSync(pageFile(route))) throw new Error(`Retired route was regenerated: ${route}`);
}
console.log(`Verified ${routes.length} portfolio routes, retired-route absence and base ${base}`);