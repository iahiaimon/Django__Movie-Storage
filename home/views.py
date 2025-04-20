from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm , AddMovieForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CustomUserForm()

    return render(request , 'register.html' , {'form': form} )



def addmovie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = AddMovieForm()
    
    return render(request , 'addmovie.html' , {'form' : form})