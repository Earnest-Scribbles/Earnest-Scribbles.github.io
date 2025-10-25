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
  }), pagefind()],
});