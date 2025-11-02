import { defineConfig } from 'astro/config';
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import tailwind from '@astrojs/tailwind';
import pagefind from "astro-pagefind";

// https://astro.build/config
export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  integrations: [tailwind({
    applyBaseStyles: false,
  }), pagefind({
    indexing: {
      markdown: {
        excerpt: true,
        // Use the page's main h1 (PageHeading) so the site logo's h1 doesn't get picked up
        fields: [
          {
            name: "title",
            selector: "main h1",
            indexed: true,
            displayed: true
          },
          "description"
        ]
      },
      selectors: {
        // Prefer the main heading, then article heading, then document <title>
        "article": "article",
        "title": ["main h1", "article h1", "title", ".title"]
      }
    }
  })],
});