const normalize = (value: string) => value.replace(/^\/+|\/+$/g, "");

export function internalPath(path = "/") {
  const value = normalize(path);
  return value ? `/${value}/` : "/";
}

export function href(path = "/") {
  return new URL(internalPath(path).replace(/^\//, ""), import.meta.env.BASE_URL).pathname;
}

export function asset(path: string) {
  return href(path);
}

export const paths = {
  home: () => href("/"),
  projects: () => href("/projects"),
  project: (id: string) => href(`/projects/${id}`),
  blog: () => href("/blog"),
  post: (id: string) => href(`/blog/${id}`),
  cv: (id: string) => href(`/cv/${id}`),
  focus: (id: string) => href(`/focus/${id}`),
  contact: () => href("/contact")
};
