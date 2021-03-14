# Generated by Django 3.1.3 on 2020-12-07 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20201203_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default=datetime.datetime(2020, 12, 7, 11, 13, 46, 108223, tzinfo=utc), max_length=500, verbose_name='Muallifi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name="ko'rildi"),
        ),
    ]