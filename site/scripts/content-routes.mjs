import { readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const contentRoot = join(scriptDir, "..", "src", "content");

function ids(collection) {
  return readdirSync(join(contentRoot, collection), { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => entry.name.slice(0, -3))
    .sort();
}

export function portfolioRoutes() {
  return [
    "/",
    "/projects/",
    ...ids("projects").map((id) => `/projects/${id}/`),
    "/blog/",
    ...ids("posts").map((id) => `/blog/${id}/`),
    ...ids("cv").map((id) => `/cv/${id}/`),
    "/contact/"
  ];
}
