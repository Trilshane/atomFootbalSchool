// app/blog/page.tsx
import Image from "next/image";
import { normalizeMediaUrl } from "../../../lib/image-utils";

// 🔥 Отдельная функция для получения данных
async function getPosts() {
  const API_URL = process.env.API_URL || "http://backend:8000";
  const endpoint = `${API_URL}/api/posts/`;

  const res = await fetch(endpoint, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    cache: "no-store",
    next: { revalidate: 0 },
  });

  if (!res.ok) {
    const errorText = await res.text();
    throw new Error(`API вернул ${res.status}: ${errorText.slice(0, 300)}`);
  }

  const posts = await res.json();
  if (!Array.isArray(posts)) {
    throw new Error(
      `API вернул не массив: ${JSON.stringify(posts).slice(0, 200)}`,
    );
  }

  return posts;
}

export const dynamic = "force-dynamic";

export default async function BlogPage() {
  const posts = await getPosts();
  console.log(posts);

  return <div className="container"></div>;
}
