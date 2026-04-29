from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    # Превращает список ID категорий в список их названий
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ["id", "title", "text", "categories", "news_image", "created_at"]