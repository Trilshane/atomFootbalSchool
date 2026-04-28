/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,

  images: {
    unoptimized: true, // ⚡ Отключает оптимизатор для dev-режима
    remotePatterns: [
      {
        protocol: "http",
        hostname: "localhost",
        port: "8000",
        pathname: "/media/**",
      },
      {
        protocol: "http",
        hostname: "backend",
        port: "8000",
        pathname: "/media/**",
      },
    ],
  },
};

export default nextConfig;
