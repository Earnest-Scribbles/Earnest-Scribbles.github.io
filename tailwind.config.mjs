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
			}
		},
	},
	plugins: [],
}
