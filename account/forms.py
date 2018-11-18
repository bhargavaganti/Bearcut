from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignupForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Choosen password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type password again'}))

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
