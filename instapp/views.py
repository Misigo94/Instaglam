from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q, query
# Create your views here.
@login_required(login_url='/registration/login/')
def home(request):
    post=Image.objects.all()
    form = CommentsForm(request.POST)
    if request.method == 'POST':

            if form.is_valid():
                form.save()
            return HttpResponse("your comment was successfully submitted")
    return render(request, 'index.html',{'post':post,"form":form})
    # return render (request,'index.html')


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            # form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.success(request,('there was an error logging in, please try again...'))
                return redirect('login')
    else:
        return render (request,'registration/login.html', {'form':form})
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

# def display(request):
#     post=Image.objects.all()
#     form = CommentsForm
#     if request.method == 'POST':

#             if form.is_valid():
#                 form.save()
#             return HttpResponse("your comment was successfully submitted")
#     return render(request, 'index.html',{'post':post})

def comments(request):
    comm_form=CommentsForm(request.POST)
    if request.method == 'POST':

            if comm_form.is_valid():
                comm_form.save()
            return redirect("/profile")
        
    return render(request,'profile.html',{'comm_form':comm_form})

# def search(request):
#     # query = None
#     # result = []
#     # if request.method == 'GET':
#     #     query = request.GET.get('search')
#     #     result = Profile.objects.filter(Q(username_icontains=query))
#     #     return render(request,'search.html',{'result':result},{'query':query})

def search(request):
    query = request.GET.get('q','')
    #The empty string handles an empty "request"
    if query:
            queryset = (Q(username__icontains=query))
            #I assume "text" is a field in your model
            #i.e., text = model.TextField()
            #Use | if searching multiple fields, i.e., 
            #queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
            results = Profile.objects.filter(queryset).distinct()
    else:
       results = []
    return render(request, 'search.html', {'results':results, 'query':query})


