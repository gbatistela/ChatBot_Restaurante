import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "https://chatbot-restaurante.onrender.com", // Cambia esto a tu URL de backend
        changeOrigin: true,
        secure: true,
      },
    },
  },
});
