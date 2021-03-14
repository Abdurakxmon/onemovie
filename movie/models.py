from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# first class

class Category(models.Model):
	name = models.CharField('Kategoriya nomi', max_length=50)
	slug = models.SlugField('*', unique=True, max_length=50)
	desc = models.TextField('Kategoriya haqida', blank=True, max_length=1500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def get_absolute_url(self):
		return reverse('movie:category_view',kwargs={'category_slug':self.slug})
# end first class


# second class


# end second class

# thirt class

class Genre(models.Model):
	name = models.CharField('Janr nomi', max_length=50)
	slug = models.SlugField('*', unique=True, max_length=50)
	desc = models.TextField('Janr haqida', blank=True, max_length=500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Janr'
		verbose_name_plural = 'Janrlar'

#end  thirt class

# 4- class

class Directors(models.Model):
	name = models.CharField('Ismi: ', max_length=80)
	age = models.PositiveIntegerField('Yoshi: ', default=0)
	country = models.CharField('Millati, Davlati: ', max_length=50)
	desc = models.TextField('Rejissor haqida: ', blank=True)
	movie = models.ForeignKey('Movie', on_delete=models.CASCADE,related_name='film_director', null=True)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Rejissor'
		verbose_name_plural = 'Rejissorlar'

class Actor(models.Model):
	name = models.CharField("Ismi", max_length=80)
	karyera = models.TextField('karyera',)
	slug = models.SlugField('*',unique=True)
	boyi = models.PositiveIntegerField('Bo\'yi',default=0)
	birth =  models.DateField("Tug'ilgan kuni", default=datetime.today)
	country =  models.CharField("Tug'ilgan joyi", max_length=500)
	desc = RichTextField(verbose_name='About Actor')
	image = models.ImageField()
	nation = models.CharField("Millati",max_length=500)
	lang = models.CharField('Tili',max_length=50)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Aktyor'
		verbose_name_plural = 'Aktyorlar'

	def get_actor(self):
		return reverse('movie:actor_detail', kwargs={'slug':self.slug})
		
class Movie(models.Model):
	title = models.CharField('Film nomi', max_length=250)
	slug = models.SlugField('*', unique=True)
	tagline = models.CharField('Film haqida qisqacha', max_length=500, default='', blank=False)
	desc = RichTextField()
	views = models.PositiveIntegerField('Ko`rildi', default=0, blank=True, null=True)

	likes = models.ManyToManyField(User, blank=True, related_name='likes')
	
	poster = models.ImageField('Film posteri', upload_to='movie/')
	year = models.PositiveIntegerField('Chiqqan sanasi', default='2020')
	country = models.CharField('Davlat', max_length=30)
	actors = models.ManyToManyField(Actor, verbose_name='aktyorlar', related_name='film_actor')
	genres = models.ManyToManyField(Genre, verbose_name='Janrlar')
	world_premiere = models.DateField("Jahondagi premyera sanasi", default=datetime.today)
	budget = models.PositiveIntegerField("Byudjet", default=0, help_text="Ko'kida ko'rsatin")
	category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	def total_likes(self):
		return self.likes.count()
	class Meta:
		verbose_name = 'Film'
		verbose_name_plural = 'Filmlar'

	def get_movie(self):
		return reverse('movie:movie_detail', kwargs={'movie_slug':self.slug})
# end class 4



# class 5
class Movie_Shots(models.Model):
	title = models.CharField('Nomi', max_length=150)
	desc = models.TextField("Kadr haqida")
	image = models.ImageField('Kadr', upload_to="movie_shots/")
	movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Kadr'
		verbose_name_plural = 'Kadrlar'
# end class 5


# class 6

class RatingStar(models.Model):
	value = models.PositiveIntegerField("Qiymat", default=0)

	def __str__(self):
		return self.value


	class Meta:
		verbose_name = 'Yulduz reytingi'
		verbose_name_plural = 'Yulduz reytinglari'
# end class 6


#class 7

class Rating(models.Model):
	ip = models.CharField('IP manzil', max_length=15)
	star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='yulduz')
	movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='film')


	def __str__(self):
		return f"{self.star} - {self.movie}"


	class Meta:
		verbose_name = 'Reying'
		verbose_name_plural = 'Reytinglar'
# end class-7

class Reviews(models.Model):
	name = models.CharField('Ism',max_length=90)
	email = models.EmailField('Ism',)
	message = models.TextField('Ism',blank=True)

	parent = models.ForeignKey(
		'self',verbose_name = 'parent',on_delete=models.SET_NULL,null=True,blank = True
		)

	movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie_comments')

	class Meta:
		verbose_name='Muhokama'
		verbose_name_plural='Muhokamalar'

	def __str__(self):
		return self.name



class News(models.Model):
	title = models.CharField('Yangilik nomi', max_length=5000)
	slug = models.SlugField('*', unique=True)
	desc = RichTextField()
	category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	image = models.ImageField('Yangilik rasmi', upload_to='movie/')
	author = models.CharField('Muallifi',max_length=500)
	views = models.PositiveIntegerField('ko\'rildi',default=0)
	date = models.DateTimeField('post sanasi', auto_now_add=True)
	category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.SET_NULL, null=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Yangilik'
		verbose_name_plural = 'Yangiliklar'

	def get_news(self):
		return reverse('movie:news_detail', kwargs={'slug':self.slug})