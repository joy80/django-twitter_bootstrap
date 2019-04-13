from django.shortcuts import render
from .forms import UserForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            messages.info(request, 'Registration successfull!')
            user_form = UserForm()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
