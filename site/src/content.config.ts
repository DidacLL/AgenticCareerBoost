import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const common = {
  title: z.string(),
  description: z.string(),
  label: z.string().optional()
};

export const collections = {
  pages: defineCollection({
    loader: glob({ base: "./src/content/pages", pattern: "**/*.md" }),
    schema: z.object(common)
  }),
  projects: defineCollection({
    loader: glob({ base: "./src/content/projects", pattern: "**/*.md" }),
    schema: z.object({
      ...common,
      summary: z.string(),
      order: z.number(),
      tags: z.array(z.string()),
      image: z.string(),
      imageAlt: z.string(),
      repository: z.string().url().optional(),
      status: z.string().optional()
    })
  }),
  posts: defineCollection({
    loader: glob({ base: "./src/content/posts", pattern: "**/*.md" }),
    schema: z.object({
      ...common,
      date: z.coerce.date(),
      tags: z.array(z.string()),
      image: z.string().optional(),
      imageAlt: z.string().optional()
    })
  }),
  cv: defineCollection({
    loader: glob({ base: "./src/content/cv", pattern: "**/*.md" }),
    schema: z.object({
      ...common,
      label: z.string(),
      order: z.number(),
      lanes: z.array(z.string()),
      technicalBase: z.array(z.string())
    })
  }),
  focus: defineCollection({
    loader: glob({ base: "./src/content/focus", pattern: "**/*.md" }),
    schema: z.object({
      ...common,
      label: z.string(),
      order: z.number(),
      relatedProjectIds: z.array(z.string()),
      relatedCvId: z.string()
    })
  })
};
