import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

const [outputArg, baseArg = "/"] = process.argv.slice(2);
if (!outputArg) throw new Error("Usage: node verify-build.mjs <dist> [base]");
const output = resolve(outputArg);
const base = baseArg === "/" ? "/" : `/${baseArg.replace(/^\/+|\/+$/g, "")}/`;
const routes = ["/", "/projects/", "/projects/agentic-career-boost/", "/projects/p3ctex/"];

const walk = (dir) => readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
  const path = join(dir, entry.name);
  return entry.isDirectory() ? walk(path) : [path];
});
const sourceFiles = walk(resolve("site/src"));
for (const file of sourceFiles) {
  const text = readFileSync(file, "utf8");
  if (text.includes("https://didacll.github.io") || text.includes("http://didacll.github.io") || text.includes('href="/AgenticCareerBoost/') || text.includes('src="/AgenticCareerBoost/')) throw new Error(`Host or deployment prefix found in source: ${file}`);
}
const pageFile = (route) => join(output, route === "/" ? "index.html" : route.replace(/^\//, "") + "index.html");
const deferredP2Routes = new Set(["/blog/", "/cv/ml/", "/contact/", "/focus/ml/", "/focus/agentic/", "/focus/backend/"]);
const refs = (html) => [...html.matchAll(/(?:href|src)=["']([^"'#]+)["']/gi)].map((match) => match[1]);
for (const route of routes) {
  const file = pageFile(route);
  if (!existsSync(file)) throw new Error(`Missing generated route: ${route}`);
  const html = readFileSync(file, "utf8");
  for (const required of [/<title>[^<]+<\/title>/i, /<meta name="description"/i, /<link rel="canonical"/i, /<main[ >]/i]) {
    if (!required.test(html)) throw new Error(`Missing page metadata or main region: ${route}`);
  }
  for (const reference of refs(html)) {
    if (/^(?:https?:|mailto:|tel:|data:|#)/i.test(reference)) continue;
    const clean = reference.split(/[?#]/, 1)[0];
    if (deferredP2Routes.has(clean)) continue;
    const local = clean.startsWith("/") ? clean.replace(base, "/").replace(/^\//, "") : clean;
    const resolved = join(output, local || "index.html");
    if (!existsSync(resolved) && !existsSync(join(resolved, "index.html"))) throw new Error(`Broken generated reference ${reference} from ${route}`);
  }
}
console.log(`Verified ${routes.length} P1 routes for base ${base}`);
