from django import forms
from author.models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm) :
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    class Meta :
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeUserForm(UserChangeForm) :
    password = None
    class Meta :
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
