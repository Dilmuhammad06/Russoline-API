from django import forms
from users.models import User
from russoline.models import Content
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']
        
class ContentUploadForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ["text","video","image"]