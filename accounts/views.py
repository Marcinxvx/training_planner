from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterUserForm, LoginUserForm


# Create your views here.

class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'add_form.html', {'form': form, 'button_text': 'Zarejestruj się'})
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'add_form.html', {'form': form, 'button_text': 'Zarejestruj się'})

class LoginUserView(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'add_form.html', {'form': form, 'button_text': 'Zaloguj się'})
    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        return render(request, 'add_form.html', {'form': form, 'button_text': 'Zaloguj się'})

class LogoutUserView(View):
    def get(self, request):
        return render(request, 'accounts/logout.html')
    def post(self, request):
        if request.POST.get('operation') == 'Tak':
            logout(request)
            return redirect('home')
        next_url = request.GET.get('next', 'home')
        return redirect(next_url)
