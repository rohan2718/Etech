from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact

#django use object
from django.contrib.auth.models import User
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

def login(request):
    if request.method == "POST":
        email=request.POST['email']
        username=request.POST['username']
        name=request.POST['name']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #print(email,username,name,pass1,pass2)

        #check for input (validations)
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('index')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('index')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('index')
            
        if len(name)==0 or len(email)<2 or not username.isalnum():
            messages.error(request, "PLEASE! Fill Appropriate Details.")
            return redirect('index')
        
        #user object
        
        user=User.objects.create_user(username,email,pass1)
        user.first_name=name
        user.save()
        messages.success(request,"SuccessFully Loged In !!")    
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        signupUsername=request.POST['signupUsername']
        signupPassword=request.POST['signupPassword']
        print(signupPassword)
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return redirect('index')
