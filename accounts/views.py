from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterUserForm

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
