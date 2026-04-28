from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField("Заголовок поста", max_length=255)
    text = models.TextField("Текст поста")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    categories = models.ManyToManyField("CategoriesPost", blank=True)
    news_image = models.ImageField(
        "Изображение поста",
        upload_to='news_images/',  # → media/news_images/
        null=True,
        blank=True
    )
    is_published = models.BooleanField("Показывать пост", default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class CategoriesPost(models.Model):
    name = models.CharField("Название категории", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name