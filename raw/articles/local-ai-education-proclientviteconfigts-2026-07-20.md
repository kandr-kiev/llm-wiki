---
source_url: file:///workspace/Projects/AI-Education-Pro/client/vite.config.ts
ingested: 2026-07-20
sha256: 3a73ddc8e0084c11f93b7b4e32746c39bdda4555438d06bca6713d67ccaee3c1
blog_source: local:unknown
---
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@assets': '/src/assets',
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
