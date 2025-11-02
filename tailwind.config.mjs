/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin');

export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				title: ["Love Ya Like A Sister", "sans-serif"],
				nav: ["Londrina Solid", "sans-serif"],
				body: ["Marujo", "sans-serif"],
				sketch: ["Sketch Block", "sans-serif"],
				code: ["Shadows Into Light", "sans-serif"],
				topic: ["Lexo", "sans-serif"],
				heading: ["Driving Around", "sans-serif"],
				index: ["Mathematic", "cursive"],
			},
			backgroundImage: {
				'body': "url('/common/doodle-light.jpg')"
			},
			colors: {
				'bubble-gum': '#ff77e9',
				'midnight': '#121063',
				'beige': '#f5f5dc',
				'almond': '#eed9c4',
				'bisque': '#ffe4c4',
				'tan': '#d2b48c',
				'rustic-brown': '#855141',
				'tawny': '#80471c',
				'tortilla': '#9a7b4f',
				'beaver': '#9f8170',
				'custom-teal': '#4c7582',
			},
			typography: {
				DEFAULT: {
					css: {
						'.katex': {
							fontFamily: 'Covered By Your Grace',
							fontSize: '1.5em',
							fontStyle: 'normal !important',
						},
						'.katex .mathnormal, .katex .amsrm, .katex .mathit, .katex .mathcal': {
							fontFamily: 'Covered By Your Grace !important',
							fontStyle: 'normal !important',
						},
						// '.mrel': {
						// 	fontFamily: 'KaTeX_Main',
						// 	fontStyle: 'normal !important',
						// },
					},
				},
			},
		},
	},
	plugins: [
		require('@tailwindcss/typography'),
		plugin(function ({ addVariant, e }) {
			addVariant('prose-inline-code', '&.prose :where(:not(pre)>code):not(:where([class~="not-prose"] *))');
		})
	],
}
