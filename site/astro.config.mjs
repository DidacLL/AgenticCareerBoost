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
  build: {
    format: "directory"
  },
  devToolbar: {
    enabled: false
  },
  integrations: indexable ? [sitemap()] : []
});
