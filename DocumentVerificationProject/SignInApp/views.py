from django.shortcuts import * # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import *
from .forms import *

UserA = get_user_model()

def RegisterView(request):
    message = None
    if request.method == 'POST':
        formSignIn = SignInForm(request.POST)
        username = request.POST.get('username')
        ##Checks if the user exists
        if UserA.objects.filter(username=username).exists():
            message = "User Already Exists"
        #If the user does not check validity and save the form
        elif formSignIn.is_valid():
            #If the form is valid then safe to the database and redirect
            #formSignIn.save()
            userInstace = UserA(username=username)
            userInstace.set_password(request.POST.get('password'))
            userInstace.save()
            return redirect('success')
    else:
        formSignIn = SignInForm()
    
    
    return render(request,'register.html',{'form':formSignIn, 'message':message})



def success(request):
    return HttpResponse("Logged In")
# Create your views here.


def SignInView(request):
    
    if request.method == 'POST':
        formSignIn = LogInForm(request.POST)
        
        if formSignIn.is_valid():
            usernameInput = request.POST.get('username')
            passwordInput = request.POST.get('password')
            
            userInstance = authenticate(request,username=usernameInput, password=passwordInput)
                
            if userInstance is not None: 
                return redirect('success')

    else:
        formSignIn = LogInForm()
    return render(request,'login.html',{'form':formSignIn}) ##The {form : formSignIn} passes the form to the html
    