/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily:{
				title: ["Love Ya Like A Sister", "sans-serif"],
				nav: ["Londrina Solid", "sans-serif"],
				body: ["Marujo", "sans-serif"],
				sketch: ["Sketch Block", "sans-serif"]
			},
			backgroundImage: {
				'body': "url('/doodle-light.jpg')"
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
				'beaver': '#9f8170'
			},
		},
	},
	plugins: [
		require('@tailwindcss/typography'),
	],
}
