import { defineConfig } from "astro/config";

export default defineConfig({
  srcDir: "./scvria/src",
  outDir: "./dist-scvria",
  output: "static",
  trailingSlash: "always",
  build: { format: "directory" },
  devToolbar: { enabled: false }
});
