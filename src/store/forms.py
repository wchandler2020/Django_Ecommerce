from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, required=True, help_text='ex: youremail@yahoo.com')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


