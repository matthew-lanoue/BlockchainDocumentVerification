from django import forms   
from .models import User
class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username":"Username",
            "password":"Password"
        }
        