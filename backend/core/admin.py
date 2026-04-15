from django.contrib import admin

from .models import Posts, CategoriesPost


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'is_published')
    list_filter = ('created_at', 'category', 'is_published')
    search_fields = ('title', 'text')
    ordering = ('-created_at',)

@admin.register(CategoriesPost)
class CategoriesPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)