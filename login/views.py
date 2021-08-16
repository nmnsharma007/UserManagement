from django.shortcuts import render
from .forms import NewUserForm
from django.contrib.auth import login
# Create your views here.
def login_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)
        # check whether form is valid
        if form.is_valid():
            user = form.save()
            login(request,user)
            
    form = NewUserForm()
    return render(request,'login/registration.html',{'form' : form})
            

