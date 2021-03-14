from .models import *
from contact.forms import ContactForm, DefaultContactForm

def view_all(request):
#	slide_movies = Movie.objects.all().order_by('-id')[:5]
#	most_popular = Movie.objects.filter(most_popular=True)
	categories = Category.objects.all()
	related_news = News.objects.all().order_by('-date')[:16]
	subscribe_form = ContactForm()
	default_form = DefaultContactForm()
	context = {
	'categories':categories,
	'related_news':related_news,
	'form_base':subscribe_form,
	'default_form': default_form,
#	'slide_movies':slide_movies,
#	'most_popular':most_popular,
	}
	return context
