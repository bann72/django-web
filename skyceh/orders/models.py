from django.db import models
from django.urls import reverse

# Create your models here.


def generate_filename(instance, filename):
    # Генерация нового имени файла, включая znum в имя файла
    import os

    basefilename, file_extension = os.path.splitext(filename)
    new_filename = f"{instance.znum}{file_extension}"
    return os.path.join("", new_filename)


# БД с основными данными о заказе
class MainOrderInfo(models.Model):
    znum = models.IntegerField(
        verbose_name="Номер заказа", primary_key=True
    )  # номер заказа
    prod = models.CharField(verbose_name="Наименование изделия")  # наименование изделия
    count = models.IntegerField(verbose_name="Количество")  # количество
    client = models.CharField(verbose_name="Название заказчика")  # название заказчика
    invorder = models.CharField(verbose_name="Счет заказа")  # счет заказа
    lastday = models.DateField(verbose_name="Срок сдачи")  # срок сдачи
    status = models.CharField(verbose_name="Статус заказа", default="В работе")
    file = models.FileField(
        upload_to=generate_filename, blank=True, null=True, verbose_name="Файл"
    )

    class Meta:
        ordering = ["-znum"]
        verbose_name = "Заказы"

    def __str__(self):
        return str(self.znum)

    def get_absolute_url(self):
        return reverse("order-detail", args=[str(self.znum)])
