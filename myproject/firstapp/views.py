from django.shortcuts import render,redirect
from .forms import ContactForm,RegistrationForm
from .models import Contact,Profile
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout




# Create your views here.

def index(request):
    context={'form':ContactForm(),'contacts':Contact.objects.all()}
    return render(request,"index.html",context)


def create_contact(request):
    if request.method =='POST':
        form=ContactForm(request.POST or None)
        if form.is_valid():
            contact=form.save()
            context={'contact':contact}
            return render(request,'partials/contact.html',context)


    return render(request,'partials/form.html',{'form':ContactForm})


def Register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()  
            Profile.objects.create(
                user=user,
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
                phone_number=user_form.cleaned_data['phone_number'],
                email=user_form.cleaned_data['email'],
            )
         
            return redirect('login')
    else:
        user_form = RegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})


def check_username(request):
    username=request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red;'>The username already exists")

    else:
        return HttpResponse("<div style='color:green;'>The username is available")


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'base.html')

        else:
            return render(request,'registration/login.html')

    else:
        return render(request,'registration/login.html')