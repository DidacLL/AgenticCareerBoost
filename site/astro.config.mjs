import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

const origin = process.env.SITE_ORIGIN || "https://example.invalid";
const base = process.env.SITE_BASE || "/";
const indexable = process.env.SITE_INDEXABLE === "true";

export default defineConfig({
  site: origin,
  base,
  output: "static",
  trailingSlash: "always",
  publicDir: "./assets",
  build: { format: "directory" },
  redirects: {
    "/dashboard/": "/projects/agentic-career-boost/",
    "/application-tracker/": "/projects/agentic-career-boost/",
    "/curriculum/": "/cv/ml/",
    "/notes/": "/blog/",
    "/hire/": "/focus/",
    "/hire/ml/": "/focus/ml/",
    "/hire/agentic/": "/focus/agentic/",
    "/hire/backend/": "/focus/backend/"
  },
  integrations: indexable ? [sitemap()] : []
});
