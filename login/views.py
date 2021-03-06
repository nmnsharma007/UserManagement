from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm # import a form for logging a user in
# Create your views here.

def home_page(request):
    return render(request,'login/home.html')

def registration_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)
        # check whether form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save() # save the user and return the instance
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect('home_page')
    else:
        form = NewUserForm()
    return render(request,'login/registration.html',{'form' : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")   
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request,'login/login.html',context={'form' : form})

def logout_view(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('home_page')




            

