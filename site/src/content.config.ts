import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const common = z.object({
  title: z.string(),
  description: z.string(),
  label: z.string().optional(),
  subtitle: z.string().optional()
});

const facts = z.array(z.object({ term: z.string(), value: z.string() }));

const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: common.extend({ facts: facts.optional() })
});

const projects = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: common.extend({
    summary: z.string(),
    order: z.number(),
    tags: z.array(z.string()),
    image: z.string(),
    imageAlt: z.string(),
    repository: z.string().url().optional(),
    status: z.string().optional()
  })
});

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: common.extend({
    date: z.coerce.date(),
    tags: z.array(z.string()),
    image: z.string().optional(),
    imageAlt: z.string().optional()
  })
});

const cv = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/cv" }),
  schema: common.extend({
    order: z.number(),
    lanes: z.array(z.string()),
    technicalBase: facts
  })
});

export const collections = { pages, projects, posts, cv };
