from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_protect

from .forms import SignUpForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

@csrf_protect
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home_name')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

