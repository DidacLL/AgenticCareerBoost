import { existsSync, readdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const scriptDir = dirname(scriptPath);
const contentRoot = join(scriptDir, "..", "src", "content");

export const locales = ["en", "es", "ca"];
export const defaultLocale = "en";
const translatedLocales = locales.filter((locale) => locale !== defaultLocale);
const requiredPages = ["home", "projects", "blog", "contact", "footer", "not-found"];

function sourceDir(collection, locale) {
  return locale === defaultLocale ? join(contentRoot, collection) : join(contentRoot, collection, locale);
}

function ids(collection, locale) {
  const dir = sourceDir(collection, locale);
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => entry.name.slice(0, -3))
    .sort();
}

function sameIds(collection, locale) {
  const expected = ids(collection, defaultLocale);
  const actual = ids(collection, locale);
  if (expected.join("\n") !== actual.join("\n")) {
    throw new Error(`${collection}: ${locale} translations do not match English ids. expected=${expected.join(",")} actual=${actual.join(",")}`);
  }
}

export function assertTranslationParity() {
  for (const locale of translatedLocales) {
    for (const page of requiredPages) {
      if (!existsSync(join(sourceDir("pages", locale), `${page}.md`))) {
        throw new Error(`pages: missing ${locale}/${page}.md translation`);
      }
    }
    for (const collection of ["projects", "posts", "cv"]) sameIds(collection, locale);
  }
}

const cleanRoute = (route) => route === "/" ? "/" : `/${route.replace(/^\/+|\/+$/g, "")}/`;

export function routeLocale(route) {
  const parts = cleanRoute(route).split("/").filter(Boolean);
  return translatedLocales.includes(parts[0]) ? parts[0] : defaultLocale;
}

export function semanticRoute(route) {
  const normalized = cleanRoute(route);
  const locale = routeLocale(normalized);
  if (locale === defaultLocale) return normalized;
  const parts = normalized.split("/").filter(Boolean).slice(1);
  return parts.length ? `/${parts.join("/")}/` : "/";
}

export function localizedRoute(route, locale) {
  const semantic = semanticRoute(route);
  if (locale === defaultLocale) return semantic;
  return semantic === "/" ? `/${locale}/` : `/${locale}${semantic}`;
}

export function portfolioRoutes() {
  assertTranslationParity();
  return locales.flatMap((locale) => [
    localizedRoute("/", locale),
    localizedRoute("/projects/", locale),
    ...ids("projects", locale).map((id) => localizedRoute(`/projects/${id}/`, locale)),
    localizedRoute("/blog/", locale),
    ...ids("posts", locale).map((id) => localizedRoute(`/blog/${id}/`, locale)),
    ...ids("cv", locale).map((id) => localizedRoute(`/cv/${id}/`, locale)),
    localizedRoute("/contact/", locale)
  ]);
}

export const retiredRoutes = [
  "/application-tracker/",
  "/dashboard/",
  "/curriculum/",
  "/curriculum/index.html",
  "/notes/",
  "/hire/",
  "/hire/ml/",
  "/hire/agentic/",
  "/hire/backend/",
  "/focus/",
  "/focus/ml/",
  "/focus/agentic/",
  "/focus/backend/"
];

if (process.argv[1] && resolve(process.argv[1]) === resolve(scriptPath)) {
  console.log(portfolioRoutes().join("\n"));
}
