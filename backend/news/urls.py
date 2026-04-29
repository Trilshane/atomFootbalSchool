from django.urls import path
from .views import PostsListAPIView

urlpatterns = [
    path('api/posts/', PostsListAPIView.as_view(), name='posts-list'),
]