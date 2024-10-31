from django.shortcuts import * # type: ignore
from django.http import HttpResponse # type: ignore
from .forms import *

def RegisterView(request):
    if request.method == 'POST':
        formSignIn = SignInForm(request.POST)
        if formSignIn.is_valid():
            formSignIn.save()
            return redirect('success')
    else:
        formSignIn = SignInForm()
    return render(request,'register.html',{'form':formSignIn}) ##The {form : formSignIn} passes the form to the html

def success(request):
    return HttpResponse("Logged In")
# Create your views here.

def SignInView(request):
    if request.method == 'POST':
        formSignIn = SignInForm(request.POST)
        if formSignIn.is_valid():
            formSignIn.save()
            return redirect('success')
    else:
        formSignIn = SignInForm()
    return render(request,'login.html',{'form':formSignIn}) ##The {form : formSignIn} passes the form to the html

