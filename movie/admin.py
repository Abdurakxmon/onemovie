from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    list_filter = ('country', 'category')
    prepopulated_fields = {
    'slug':('title',)
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth')
    list_filter = ('name',)
    prepopulated_fields = {
    'slug':('name',)
    }

@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Movie_Shots)
class MovieshotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')
    list_filter = ('title',)

@admin.register(Directors)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'age')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('email',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)
    list_filter = ('date', 'title')
    prepopulated_fields = {
    'slug':('title',)
    }


admin.site.register(RatingStar)

admin.site.register(Rating)
