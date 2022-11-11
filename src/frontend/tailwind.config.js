module.exports = {
    content: [
      "./components/**/*.{js,vue,ts}",
      "./layouts/**/*.vue",
      "./pages/**/*.vue",
      "./plugins/**/*.{js,ts}",
      "./nuxt.config.{js,ts}",
    ],
    theme: {
      extend: {
        fontFamily: {
            'title': ['Nunito', 'Arial', 'sans-serif'],
            'body': ['PT Sans', 'Arial', 'sans-serif']
        }
      },
    },
    daisyui: {
        themes: [
            {
                mytheme: {
                
                    "primary": "#8b5cf6",
                    "secondary": "#afffe3",
                    "accent": "#b10de8",
                    "neutral": "#374151",
                    "base-100": "#f3f4f6",
                    "info": "#95D8F9",
                    "success": "#4BD8A4",
                    "warning": "#D87E18",
                    "error": "#EF6B8A",
                    'fontFamily': 'PT Sans',
                    ".btn": {
                      "fontFamily": "Nunito",
                    }
                },
            },
        ],
    },
    plugins: [require("@tailwindcss/typography"), require('@tailwindcss/forms'), require("daisyui")],
}