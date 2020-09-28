from django import forms
from .models import LoginInformation, RegisterInformation, Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class FirstSignup(forms.ModelForm):
    email = forms.CharField(max_length =30, widget=forms.TextInput(attrs={"placeholder": "Email Address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    class Meta:
        model = LoginInformation
        fields = ['email', 'password']
    
class Usersignupform(UserCreationForm): 
    #email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email Address"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter Password"}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Renter Password"}))
    class Meta:
        model = RegisterInformation
        fields = ['username', 'password1', 'password2']

class RegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length='40', help_text='Add a valid email address', widget=forms.TextInput(attrs={"placeholder": "Enter a valid email address"}))
    username = forms.CharField(max_length='30', widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Renter Password"}))
    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    email=forms.EmailField(max_length='40', help_text='Add a valid email address', widget=forms.TextInput(attrs={"placeholder": "Enter a valid email address"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    class Meta:
        model = Account
        fields = {'email', 'password'}

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")

