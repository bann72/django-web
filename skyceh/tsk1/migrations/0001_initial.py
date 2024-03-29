# Generated by Django 5.0 on 2023-12-24 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('task', models.TextField(verbose_name='Задача')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('now', models.IntegerField(default=0, verbose_name='Готово')),
                ('total', models.IntegerField(default=1, verbose_name='Всего')),
                ('spot', models.CharField(choices=[(None, 'Выберите участок'), ('плазма', 'плазма')], max_length=30, verbose_name='Участок')),
                ('man', models.CharField(max_length=30, verbose_name='ФИО сотрудника')),
                ('deadline', models.DateField(default=datetime.date.today, verbose_name='Срок')),
                ('ready', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Задачи',
                'ordering': ['-dat'],
            },
        ),
    ]
