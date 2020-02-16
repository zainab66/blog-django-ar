from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def services(request):
    return render(request, 'blog/services.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Subject = request.POST['subject']
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s" % (name, message, email)

        send_mail(Subject,
                  contact_message,
                  email,
                  to_email,
                  fail_silently=True)
    return render(request, 'blog/contact.html')
