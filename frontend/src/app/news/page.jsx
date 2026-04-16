import { cookies } from "next/headers";

export const dynamic = "force-dynamic"; // 🔥 Гарантируем динамический рендеринг

export default async function NewsPage() {
  const cookieStore = await cookies();

  // 🔥 Умный выбор URL: сервер использует имя сервиса, клиент — localhost
  const API_URL = process.env.API_URL || "http://backend:8000";
  const endpoint = `${API_URL}/api/posts/`;

  console.log("🔄 Fetching (server-side) from:", endpoint);

  try {
    const res = await fetch(endpoint, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // CSRF не нужен для GET-запросов!
      },
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

    // ✅ Рендеринг (ваш код)
    return (
      <main className="min-h-screen bg-gray-50 py-10 px-4">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-4xl font-bold text-gray-900 mb-8 text-center">
            📢 Новости школы
          </h1>
          {posts.length === 0 ? (
            <p className="text-center text-gray-500 text-lg">
              Новостей пока нет.
            </p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {posts.map((post) => (
                <article
                  key={post.id}
                  className="bg-white rounded-xl shadow-sm border p-5"
                >
                  <h2 className="text-xl font-semibold mb-2">{post.title}</h2>
                  <p className="text-gray-600 text-sm line-clamp-3">
                    {post.text}
                  </p>
                </article>
              ))}
            </div>
          )}
        </div>
      </main>
    );
  } catch (error) {
    console.error("❌ Ошибка при загрузке новостей:", error);
    return (
      <main className="p-8 text-red-700 bg-red-50 min-h-screen">
        <h1 className="text-2xl font-bold mb-4">⚠️ Ошибка загрузки новостей</h1>
        <pre className="bg-white p-4 rounded border text-sm whitespace-pre-wrap break-words">
          {error.message}
        </pre>
        <div className="mt-6 text-gray-700">
          <p className="mb-2">
            <strong>Что проверить:</strong>
          </p>
          <ol className="list-decimal list-inside space-y-1">
            <li>
              Запущен ли бэкенд? → <code>docker compose ps</code>
            </li>
            <li>
              Правильный ли URL? → <code>http://localhost:8000/api/posts/</code>
            </li>
            <li>
              Логи Django → <code>docker compose logs backend</code>
            </li>
          </ol>
        </div>
      </main>
    );
  }
}
