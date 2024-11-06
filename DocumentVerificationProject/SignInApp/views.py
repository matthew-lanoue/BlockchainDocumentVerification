from django.shortcuts import * # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import *
from  .models import *
from .forms import *
import hashlib

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
            return redirect('signInPage')
    else:
        formSignIn = SignInForm()
    
    
    return render(request,'register.html',{'form':formSignIn, 'message':message})



def success(request):
    return HttpResponse("Logged In")
# Create your views here.

def WelcomePageView(request):
    return render(request, 'welcome.html')

def UploadPortalView(request):
    # This statement below is used to redirect the user if they have not signed in
    if not request.user.is_authenticated:
        return redirect("signInPage")

    title = None
    if request.method == 'POST':
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            title = uploaded_file.name
            fileContent = uploaded_file.read()
            fileHash = hashlib.sha256(fileContent).hexdigest()
            docuInstace = Document(docname=title, fileHash=fileHash)
            docuInstace.save()
            ##This line below sets the author of the document
            docuInstace.authors.set([request.user])
            
    else:
        form = DocumentsForm()
    return render(request, 'UploadPortal.html', {'form':DocumentsForm, 'title':title})

def SignInView(request):
    #**LOGS OUT USER** 
    logout(request) 
    #*****************
    if request.method == 'POST':
        formSignIn = LogInForm(request.POST)
        
        if formSignIn.is_valid():
            usernameInput = request.POST.get('username')
            passwordInput = request.POST.get('password')
            
            userInstance = authenticate(request,username=usernameInput, password=passwordInput)
                
            if userInstance is not None: 
                login(request, userInstance)
                return redirect('UploadPage')
    else:
        formSignIn = LogInForm()
    return render(request,'login.html',{'form':formSignIn}) ##The {form : formSignIn} passes the form to the html
    