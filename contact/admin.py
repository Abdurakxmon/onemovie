from django.contrib import admin
from .models import Contact, DefaultContact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email',]
    list_filter = ('email',)

@admin.register(DefaultContact)
class DefaultContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'subject']
    list_filter = ('subject', 'email')
