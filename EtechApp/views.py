from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)
        if len(name)==0 or len(email)<0 or len(phone) < 10 or len(desc)<3:
            messages.error(request, "PLEASE! Fill Appropriate Details.")
        else:
            contact=Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request, "Message has been sent Successfully")
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')