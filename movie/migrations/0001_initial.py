# Generated by Django 3.1.2 on 2020-12-02 01:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Ismi')),
                ('karyera', models.CharField(max_length=8000, verbose_name='Karyera')),
                ('slug', models.PositiveIntegerField(default=0, verbose_name="Bo'yi")),
                ('birth', models.DateField(default=datetime.datetime.today, verbose_name="Tug'ilgan kuni")),
                ('country', models.CharField(max_length=500, verbose_name="Tug'ilgan joyi")),
                ('desc', models.TextField(max_length=1500, verbose_name='Aktor haqida')),
                ('image', models.ImageField(upload_to='')),
                ('nation', models.CharField(max_length=500, verbose_name='Millati')),
                ('lang', models.CharField(max_length=50, verbose_name='Tili')),
            ],
            options={
                'verbose_name': 'Aktyor',
                'verbose_name_plural': 'Aktyorlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya nomi')),
                ('slug', models.SlugField(unique=True, verbose_name='*')),
                ('desc', models.TextField(blank=True, max_length=1500, verbose_name='Kategoriya haqida')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Janr nomi')),
                ('slug', models.SlugField(unique=True, verbose_name='*')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Janr haqida')),
            ],
            options={
                'verbose_name': 'Janr',
                'verbose_name_plural': 'Janrlar',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Film nomi')),
                ('slug', models.SlugField(unique=True, verbose_name='*')),
                ('tagline', models.CharField(default='', max_length=500, verbose_name='Film haqida qisqacha')),
                ('desc', models.TextField(verbose_name='Film')),
                ('poster', models.ImageField(upload_to='movie/', verbose_name='Film posteri')),
                ('year', models.PositiveIntegerField(default='2020', verbose_name='Chiqqan sanasi')),
                ('country', models.CharField(max_length=30, verbose_name='Davlat')),
                ('world_premiere', models.DateField(default=datetime.datetime.today, verbose_name='Jahondagi premyera sanasi')),
                ('budget', models.PositiveIntegerField(default=0, help_text="Ko'kida ko'rsatin", verbose_name='Byudjet')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movie.Actor', verbose_name='aktyorlar')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Kategoriya')),
                ('genres', models.ManyToManyField(to='movie.Genre', verbose_name='Janrlar')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmlar',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0, verbose_name='Qiymat')),
            ],
            options={
                'verbose_name': 'Yulduz reytingi',
                'verbose_name_plural': 'Yulduz reytinglari',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Ism')),
                ('email', models.EmailField(max_length=254, verbose_name='Ism')),
                ('message', models.TextField(blank=True, verbose_name='Ism')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comments', to='movie.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.reviews', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Muhokama',
                'verbose_name_plural': 'Muhokamalar',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP manzil')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movie.movie', verbose_name='film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ratingstar', verbose_name='yulduz')),
            ],
            options={
                'verbose_name': 'Reying',
                'verbose_name_plural': 'Reytinglar',
            },
        ),
        migrations.CreateModel(
            name='Movie_Shots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('desc', models.TextField(verbose_name='Kadr haqida')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Kadr')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Film')),
            ],
            options={
                'verbose_name': 'Kadr',
                'verbose_name_plural': 'Kadrlar',
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Ismi: ')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Yoshi: ')),
                ('country', models.CharField(max_length=50, verbose_name='Millati, Davlati: ')),
                ('desc', models.TextField(blank=True, verbose_name='Rejissor haqida: ')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_director', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Rejissor',
                'verbose_name_plural': 'Rejissorlar',
            },
        ),
    ]