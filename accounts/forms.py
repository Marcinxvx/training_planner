from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from training.models import WorkoutPlan

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = ''

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'experience_in_months', 'age', 'additional_info']
        labels = {
            'height': 'Wzrost',
            'weight': 'Waga',
            'experience_in_months': 'Staż w miesiącach',
            'age': 'Wiek',
            'additional_info': 'Dodatkowe informacje'
        }

class WorkoutPlanSelectForm(forms.Form):
    workout_plan_name = forms.ModelChoiceField(label="Nazwa planu", queryset=WorkoutPlan.objects.none())
