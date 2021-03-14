from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.DefaultContactView.as_view(), name='DefaultContactView'),
]
