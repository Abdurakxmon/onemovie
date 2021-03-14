from django.urls import path
from .import views
from .models import *

app_name = 'movie'
urlpatterns = [
    path('', views.MoviesView.as_view(), name='movies_list'),
    path('subscribe/', views.email_sender, name='email_sender'),
    path('<str:movie_slug>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('add_comment/<int:movie_id>/', views.AddComment.as_view(), name='addcomment_view'),
    path('movies_list/', views.List.as_view(), name='list'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
    path('results/', views.FilterMoviesView.as_view(), name='search_result'),
    path('likes/', views.like_movie, name='likes'),
    path('news/', views.News.as_view(), name='news'),
    path('news/<str:slug>/', views.NewsView.as_view(model=News), name='news_detail'),
    path('category/<str:category_slug>/', views.CategoryMoviesView.as_view(), name='category_view'),
   

]
handler404 = 'movie.views.handler404'

