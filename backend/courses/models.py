from django.db import models

class Course(models.model):
    title = models.CharField("Название курса", max_length=255)
    total_lessons = models.PositiveIntegerField("Всего занятий в курсе")
    is_active = models.BooleanField("Показывать ли курс")
    def __str__(self):
        return self.title
    
class CourseLesson(models.model):
    title = models.CharField("Название урока", max_length=255)
    course = models.ForeignKey(Course, verbose_name="Курс к которому относится урок", on_delete=models.CASCADE)
    

