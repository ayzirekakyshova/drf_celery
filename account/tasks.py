from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_acitivation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate{activation_code}'
    message = f'Активируйте аккаунт, перейдя по ссылке\n{activation_link}'
    send_mail('Acivate account', message, 'ayzirekakyshova04@gmail.com',[email])