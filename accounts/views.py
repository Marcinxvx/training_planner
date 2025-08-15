from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views import View

from training.forms import CreateWorkoutPlanForm
from training.models import WorkoutPlan
from .forms import RegisterUserForm, LoginUserForm, UserProfileForm
from .models import UserProfile


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
        if request.POST.get('operation') == 'Yes':
            logout(request)
            return redirect('home')
        next_url = request.GET.get('next', 'home')
        return redirect(next_url)

class CreateUserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            user_profile = request.user.userprofile
            context = {'user_profile': user_profile, 'profile_exists': True}
        except UserProfile.DoesNotExist:
            form = UserProfileForm()
            context = {'form': form, 'profile_exists': False}
        return render(request, 'accounts/create_user_profile.html', context)
    def post(self, request):
        try:
            if request.user.userprofile:
                return redirect('create_user_profile')
        except UserProfile.DoesNotExist:
            form = UserProfileForm(request.POST)
            if form.is_valid():
                user_profile = form.save(commit=False)
                user_profile.user = request.user
                user_profile.save()
                return redirect('create_user_profile')
            return render(request, 'accounts/create_user_profile.html', {'form': form,'profile_exists': False})

class UpdateUserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=user_profile)
        return render(request, 'accounts/update_user_profile.html', {'form': form, 'user_profile': user_profile})
    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('create_user_profile')
        return render(request, 'accounts/update_user_profile.html', {'form': form, 'user_profile': user_profile})

class DeleteUserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'accounts/delete_user_profile.html', {'user_profile': user_profile})
    def post(self, request):
        if request.POST.get('operation') == 'Yes':
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.delete()
        return redirect('create_user_profile')
