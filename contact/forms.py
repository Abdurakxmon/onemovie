from .models import Contact, DefaultContact
from django import forms
from django.forms import Textarea

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email',)

class DefaultContactForm(forms.ModelForm):
    class Meta:
        model = DefaultContact
        fields = ('first_name', 'last_name', 'subject', 'email', 'message',)
        widgets = {
            'message': Textarea(attrs={"autocomplete":"off", 'cols':30, 'rows':8}),
        }
