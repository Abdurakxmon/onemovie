from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Someone has tried to login your account',
        'Please enter your password to save for verification, otherwise, it may fail to be secured by Google',
        'jamolxonahmedov124@mail.ru',
        [user_email],
        fail_silently = False
    )
