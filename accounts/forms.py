from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
