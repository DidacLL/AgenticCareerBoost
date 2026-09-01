import type { NavId } from "../data/site";

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

const navigationRoutes: Record<NavId, string> = {
  home: "/",
  projects: "/projects",
  blog: "/blog",
  cv: "/cv/ml",
  focus: "/focus",
  contact: "/contact"
};

export const paths = {
  home: () => href("/"),
  nav: (id: NavId) => href(navigationRoutes[id]),
  projects: () => href("/projects"),
  project: (id: string) => href(`/projects/${id}`),
  blog: () => href("/blog"),
  post: (id: string) => href(`/blog/${id}`),
  cv: (id: string) => href(`/cv/${id}`),
  focus: (id?: string) => href(id ? `/focus/${id}` : "/focus"),
  contact: () => href("/contact")
};

export function semanticPath(pathname: string) {
  const base = import.meta.env.BASE_URL;
  if (base !== "/" && pathname.startsWith(base)) {
    return internalPath(pathname.slice(base.length));
  }
  return pathname.endsWith(".html") ? pathname : internalPath(pathname);
}