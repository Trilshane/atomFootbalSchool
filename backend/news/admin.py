from django.contrib import admin

from .models import Posts, CategoriesPost


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'get_categories', 'is_published')
    list_filter = ('created_at', 'categories', 'is_published')
    search_fields = ('title', 'text')
    ordering = ('-created_at',)

    
    @admin.display(description='Категории')
    def get_categories(self, obj):
        # Собираем названия категорий через запятую
        return ", ".join(cat.name for cat in obj.categories.all())

@admin.register(CategoriesPost)
class CategoriesPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)