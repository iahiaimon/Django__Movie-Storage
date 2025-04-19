from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number' , 'password1' , 'password2')


