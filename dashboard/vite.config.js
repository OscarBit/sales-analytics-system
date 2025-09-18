import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // This is important for Docker
    proxy: {
      '/api': {
        target: 'http://web:8000', // <-- Use the service name 'web'
        changeOrigin: true,
      },
    },
  },
})
