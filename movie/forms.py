from django.forms import ModelForm, Textarea
from .models import Reviews

class CommentForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 8}),
        }