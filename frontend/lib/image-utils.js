// frontend/lib/image-utils.js
export function normalizeMediaUrl(url) {
  if (!url) return "";

  // Если URL уже абсолютный и содержит backend:8000
  if (url.includes("backend:8000")) {
    return url.replace(
      "http://backend:8000",
      process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
    );
  }

  // Если URL относительный (/media/...)
  if (url.startsWith("/media/")) {
    return `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}${url}`;
  }

  // Если уже содержит localhost или другой домен — возвращаем как есть
  return url;
}
