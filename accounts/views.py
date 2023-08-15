from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm


class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('phone'), password=cd.get('password'))
            if user is not None:
                login(request, user)
                return redirect('accounts:login_user')
            else:
                form.add_error('phone', 'Your phone number or password is incorrect')
        return render(request, 'accounts/login.html', {'form': form})


class LogoutUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
