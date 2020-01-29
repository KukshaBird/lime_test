from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from .forms import SignupForm, UserLoginForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "auth/login.html"


#  Function views
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request, 'base.html')
