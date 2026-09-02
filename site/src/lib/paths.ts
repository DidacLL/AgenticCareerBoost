import type { NavId } from "../data/site";
import { defaultLocale, isLocale, type Locale } from "./i18n";

const normalize = (value: string) => value.replace(/^\/+|\/+$/g, "");

export function internalPath(path = "/") {
  const value = normalize(path);
  return value ? `/${value}/` : "/";
}

export function href(path = "/") {
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  return `${base}${internalPath(path)}`;
}

export function asset(path: string) {
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  return `${base}/${normalize(path)}`;
}

export function localizedInternalPath(path = "/", locale: Locale = defaultLocale) {
  const semantic = internalPath(path);
  return locale === defaultLocale ? semantic : internalPath(`/${locale}${semantic}`);
}

export function localizedHref(path = "/", locale: Locale = defaultLocale) {
  return href(localizedInternalPath(path, locale));
}

const navigationRoutes: Record<NavId, string> = {
  home: "/",
  projects: "/projects",
  blog: "/blog",
  cv: "/cv/ml",
  contact: "/contact"
};

export const paths = {
  home: (locale: Locale = defaultLocale) => localizedHref("/", locale),
  nav: (id: NavId, locale: Locale = defaultLocale) => localizedHref(navigationRoutes[id], locale),
  projects: (locale: Locale = defaultLocale) => localizedHref("/projects", locale),
  project: (id: string, locale: Locale = defaultLocale) => localizedHref(`/projects/${id}`, locale),
  blog: (locale: Locale = defaultLocale) => localizedHref("/blog", locale),
  post: (id: string, locale: Locale = defaultLocale) => localizedHref(`/blog/${id}`, locale),
  cv: (id: string, locale: Locale = defaultLocale) => localizedHref(`/cv/${id}`, locale),
  contact: (locale: Locale = defaultLocale) => localizedHref("/contact", locale)
};

export function semanticPath(pathname: string) {
  const base = import.meta.env.BASE_URL;
  if (base !== "/" && pathname.startsWith(base)) {
    return internalPath(pathname.slice(base.length));
  }
  return pathname.endsWith(".html") ? pathname : internalPath(pathname);
}

export function stripLocale(pathname: string) {
  const semantic = semanticPath(pathname);
  if (semantic.endsWith(".html")) return semantic;
  const parts = normalize(semantic).split("/").filter(Boolean);
  if (parts.length && isLocale(parts[0])) parts.shift();
  return internalPath(parts.join("/"));
}

export function switchLocaleHref(pathname: string, locale: Locale) {
  return localizedHref(stripLocale(pathname), locale);
}

export function localizedSemanticPath(pathname: string, locale: Locale) {
  return localizedInternalPath(stripLocale(pathname), locale);
}
