from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer


class PostsListAPIView(generics.ListAPIView):
    """
    API-эндпоинт для получения списка опубликованных постов.
    Метод: GET
    URL: /api/posts/
    Ответ: JSON-массив постов
    """
    # Какие данные брать из базы
    queryset = Posts.objects.filter(
        is_published=True
    ).prefetch_related('categories').order_by('-created_at')
    
    # Как сериализовать (превратить в JSON)
    serializer_class = PostSerializer