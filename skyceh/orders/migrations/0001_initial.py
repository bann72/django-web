# Generated by Django 5.0 on 2023-12-24 20:00

import orders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainOrderInfo',
            fields=[
                ('znum', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа')),
                ('prod', models.CharField(verbose_name='Наименование изделия')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('client', models.CharField(verbose_name='Название заказчика')),
                ('invorder', models.CharField(verbose_name='Счет заказа')),
                ('lastday', models.DateField(verbose_name='Срок сдачи')),
                ('status', models.CharField(default='В работе', verbose_name='Статус заказа')),
                ('file', models.FileField(blank=True, null=True, upload_to=orders.models.generate_filename, verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Заказы',
                'ordering': ['-znum'],
            },
        ),
    ]