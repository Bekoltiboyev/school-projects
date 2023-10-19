from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    UserName = forms.CharField(
        label="User Name",
        min_length=3,
        max_length=50,  
        widget=forms.TextInput(attrs={"placeholder": "User Name"})
        )
    password = forms.CharField(
        label="password",
        min_length=4,
        max_length=40,
        widget=forms.TextInput(attrs={"placeholder": "password", "type":"password"})
        )
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']



class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = "__all__"
        exclude = ['profiles']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = "__all__"
        exclude = ['project', 'user_profile', 'user_profile_image']