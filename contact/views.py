from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import DefaultContact
from .forms import DefaultContactForm
from .service import send

class DefaultContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        if request.method == 'POST':
            form = DefaultContactForm(request.POST)
            if form.is_valid():
                print(form)
                form.save()
                last_user = DefaultContact.objects.all().order_by('id')[:1]
                for email in last_user:
                    if email:
                        send(email)
        else:
            form = DefaultContactForm()

        return render(request, 'contact.html', {'default_form':form})
