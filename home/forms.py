from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser , AddMovie


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number' , 'password1' , 'password2')


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        fields = ('title' , 'description' , 'catagory' , 'publish' , 'image')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'publish' : forms.DateInput(attrs={'type' : 'date'})
        }