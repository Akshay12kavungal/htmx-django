from django.shortcuts import render,redirect
from .forms import ContactForm,RegistrationForm
from .models import Contact,Profile,School
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView

from django.urls import reverse



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
    


#school crud operations

class SchoolListView(ListView):
    model=School
    template_name='school/school_list.html'
    context_object_name='school'

class SchoolDetailView(DetailView):
    model=School
    template_name='school/school_detail.html'
    context_object_name='schooldetail'

class SchoolUpdateView(UpdateView):
    model=School
    template_name='school/school_update.html'
    fields = ['name', 'principal', 'location']
    

    def get_success_url(self):
        return reverse('school_list')


class SchoolDeleteView(DeleteView):
    model=School
    template_name='school/school_delete.html'
  
    def get_success_url(self):
        return reverse('school_list')
    

class SchoolCreateView(CreateView):
    model=School
    template_name='school/school_create.html'
    context_object_name='schoolcreate'
    fields = ['name', 'principal', 'location']

    def get_success_url(self):
        return reverse('school_list')
    

