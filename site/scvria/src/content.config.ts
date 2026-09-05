import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const products = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./scvria/src/content/products" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    order: z.number(),
    status: z.enum(["active", "experimental", "archived"]),
    tags: z.array(z.string()).default([]),
    platforms: z.array(z.string()).default([]),
    repository: z.string().url().optional(),
    documentation: z.string().url().optional(),
    download: z.string().url().optional(),
    website: z.string().url().optional(),
    license: z.string().optional()
  }).strict()
});

export const collections = { products };
