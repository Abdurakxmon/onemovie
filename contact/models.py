from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        pass


class DefaultContact(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    subject = models.CharField('Subject', max_length=100)
    email = models.EmailField('Email', max_length=100)
    message = models.TextField('Message')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Default Contact'
        verbose_name_plural = 'Default Contacts'
