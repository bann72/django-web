from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    SPOTS = (
        (None, "Выберите участок"),
        ("плазма", "плазма"),
    )
    dat = models.DateField(default=date.today, verbose_name="Дата")
    task = models.TextField(verbose_name="Задача")
    file = models.FileField(blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение")
    now = models.IntegerField(default=0, verbose_name="Готово")
    total = models.IntegerField(default=1, verbose_name="Всего")
    spot = models.CharField(choices=SPOTS, max_length=30, verbose_name="Участок")
    man = models.CharField(verbose_name="ФИО сотрудника", max_length=30)
    deadline = models.DateField(default=date.today, verbose_name="Срок")
    ready = models.BooleanField(default=False)

    class Meta:
        ordering = ["-dat"]
        verbose_name = "Задачи"

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
