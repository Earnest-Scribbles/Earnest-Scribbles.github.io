// Import utilities from `astro:content`
import { z, defineCollection } from "astro:content";
import { glob } from 'astro/loaders';

// Define a `type` and `schema` for each collection
const blogsCollection = defineCollection({
    loader: glob({ pattern: '**/[^_]*.md', base: "./src/data/blogs" }),
    schema: z.object({
      title: z.string(),
      pubDate: z.date(),
      description: z.string(),
      draft: z.boolean().default(false),
      image: z.object({
        url: z.string(),
        alt: z.string()
      }),
      tags: z.array(z.string())
    })
});

const noteBookCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/data/notebooks" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    draft: z.boolean().default(false),
    image: z.object({
      url: z.string(),
      alt: z.string()
    }),
    tags: z.array(z.string())
  })
});

const projectCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/data/projects" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    draft: z.boolean().default(false),
    image: z.object({
      url: z.string(),
      alt: z.string()
    }),
    tags: z.array(z.string())
  })
});

// Export a single `collections` object to register your collection(s)
export const collections = {
  blogs: blogsCollection,
  notebooks: noteBookCollection,
  projects: projectCollection
};