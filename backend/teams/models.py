from django.db import models

class Year(models.Model):
    year = models.IntegerField("Год команды")

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Года"
        ordering = ["year"]

    def __str__(self):
        return str(self.year)


class Position(models.Model):
    position_name = models.CharField("Название позиции", max_length=255)
    position_short_name = models.CharField("Название позиции(кратко)", max_length=5)

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

    def __str__(self):
        return f"{self.position_name} ({self.position_short_name})"


class Player(models.Model):
    first_name = models.CharField("Имя игока", max_length=255)
    last_name = models.CharField("Фамилия Игрока", max_length=255)
    birth = models.DateField("Дата рождения игрока")
    position = models.ManyToManyField(
        "Position", verbose_name="Позиция игрока", blank=True
    )
    photo = models.ImageField(
        "Фото игрока", upload_to="teams/players/", null=True, blank=True
    )
    year = models.ManyToManyField("Year", verbose_name="Год игрока", blank=False)

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"
