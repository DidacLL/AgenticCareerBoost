import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

const origin = process.env.SITE_ORIGIN || "https://example.invalid";
const base = process.env.SITE_BASE || "/";
const indexable = process.env.SITE_INDEXABLE === "true";
const withBase = (path) => `${base === "/" ? "" : base.replace(/\\/$/, "")}${path}`;

export default defineConfig({
  site: origin,
  base,
  output: "static",
  trailingSlash: "always",
  publicDir: "./assets",
  build: { format: "directory" },
  redirects: {
    "/dashboard/": withBase("/projects/agentic-career-boost/"),
    "/application-tracker/": withBase("/projects/agentic-career-boost/"),
    "/curriculum/": withBase("/cv/ml/"),
    "/notes/": withBase("/blog/"),
    "/hire/": withBase("/focus/"),
    "/hire/ml/": withBase("/focus/ml/"),
    "/hire/agentic/": withBase("/focus/agentic/"),
    "/hire/backend/": withBase("/focus/backend/")
  },
  integrations: indexable ? [sitemap()] : []
});
