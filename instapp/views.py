from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render (request,'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('there ws an error loggig in, please try again...'))
            return redirect('login')
    else:
        return render (request,'registration/login.html', {})
    # return(request, 'registration/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect ('login')

def register_user(request):
    if request.method == 'POST':
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Regestration succesful'))
            return redirect('home')
    else:
        form =RegisterUserForm()
    return render(request,'registration/register.html',{'form':form,})

def upload_profile(request):
    form=ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':

            if form.is_valid():
                form.save()
            return redirect("/profile")
        
    return render(request,'profile.html',{'form':form})



