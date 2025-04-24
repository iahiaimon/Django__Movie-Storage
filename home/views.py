from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, AddMovieForm
from .models import AddMovie
from django.contrib import messages

# Create your views here.


def home(request):
    movies = AddMovie.objects.all()
    return render(request, "home.html" , {"movies" : movies})


def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = CustomUserForm()

    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.error(request, "Invalid username or password.")
        elif not user.is_verified:
            messages.error(request, "Your email is not verified yet.")
        else:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')

    return render(request, "login.html")


def addmovie(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = AddMovieForm()

    return render(request, "addmovie.html", {"form": form})
    

def deletemovie(request , id):
    movie = AddMovie.objects.get(id = id)
    movie.delete()
    return redirect('home')
