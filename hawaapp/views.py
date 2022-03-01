import email
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def LoginPage(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')

        else:
            messages.error(request, 'user is not reigstered')
    return render(request, 'registration/login.html')


def RegisterPage(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        user_email = form.cleaned_data.get('email')
        messages.success(request, "Account was created for" + user_email)
        return redirect('LoginPage')
    else:
        form = SignUpForm
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def Home(request):
    return render(request, 'home.html')
