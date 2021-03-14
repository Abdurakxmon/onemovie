from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import CreateView
from contact.models import Contact
from contact.service import send
from contact.forms import ContactForm
from django.shortcuts import render


# Create your views here.

def like_movie(request):
	movie = get_object_or_404(Movie, id=request.GET.get('data'))
	if movie.likes.filter(id=request.user.id).exists():
		movie.likes.remove(request.user)
		is_liked = False
		status = "like"
	else:
		movie.likes.add(request.user)
		is_liked=True
		status = "dislike"
	context = {
	'status':status,
	'is_liked':is_liked,
	'total_likes':movie_likes()
	}
	return JsonResponse(context)



def email_sender(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            last_user = Contact.objects.all().order_by('id')[:1]
            for email in last_user:
                if email:
                    send(email)
                return render(request, 'index.html')

    else:
        form = ContactForm()
    return render(request, 'index.html', {'form':form})


class MoviesView(View):
	""" Movies View  class """
	def get(self, request):
		movies = Movie.objects.all()

		context = {
			'movies':movies,
		}

		return render(request, 'index.html', context)

class MovieDetailView(View):
	""" Movie detail view class """

	def get(self, request, movie_slug):
		movie = get_object_or_404(Movie,slug=movie_slug)

		
		movie.views += 1
		movie.save()

		last_movies = Movie.objects.all().order_by('-id')[:8]

		context = {'movie':movie, 'l_movies':last_movies}
		return render(request, 'single.html', context)



class AddComment(View):
	def post(self,request,movie_id):
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				create = form.save(commit=False)
				if request.POST.get("parent", None):
					form.parent_id = int(request.POST.get('parent'))
				movie = get_object_or_404(Movie, id=movie_id)
				create.movie = movie
				form.save()
				return HttpResponseRedirect(reverse("movie:movie_detail",kwargs = {"movie_slug":movie.slug}))
		else:
			form = CommentForm()
			print('no'*5)
		return render(request,'single.html',{'form':form})
class FilterMoviesView(ListView):
	model = Movie
	template_name = 'list.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Movie.objects.filter(
			Q(title__icontains = query) | Q(desc__icontains = query)
			)
		return object_list

class ActorView(DetailView):
	model = Actor
	slug_field = 'name'
	template_name = 'actor_detail.html'



class List(View):
	def get(self,request):
		return render(request,"list.html")

def handler404(request, *args, **argv):
    response = render('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response


class News(ListView):
	model = News
	slug_field = 'slug'
	queryset = News.objects.all().order_by('-date')[:16]
	template_name = 'news.html'

class NewsView(DetailView):
	model = News
	slug_field = 'slug'
	template_name = 'news-single.html'


class CategoryMoviesView(ListView):
	def get(self,request,category_slug):
		category = Category.objects.get(slug=category_slug)
		movie = category.movie_set.all()

		paginator = Paginator(movie, 2) #show 2 movies per page
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		context = {'category_movie':movie,'page_obj':page_obj,}
		return render(request,'categories_list.html',context)

