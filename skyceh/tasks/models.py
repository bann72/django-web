from django.db import models

# Create your models here.


class SpotList(models.Model):
    SPOTS = ((None, "Выберите участок"), ("плазма", "плазма"))
    man = models.CharField(verbose_name="ФИО сотрудника", primary_key=True)
    spot = models.CharField(choices=SPOTS)


class TaskList(models.Model):
    date = models.DateField()
    task = models.TextField()
    file = models.FileField()
    man = models.ForeignKey(SpotList, on_delete=models.PROTECT)
    deadline = models.DateField()
