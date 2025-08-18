import pytest
from django.contrib.auth.models import User

from accounts.models import UserProfile


@pytest.fixture
def users_to_register_success():
    users = []
    for i in range(10):
        username = f'User{i}'
        password = f'Password123!@#{i}'
        users.append((username, password))
    return users

@pytest.fixture
def user_login_data():
    user = User.objects.create_user(username='Testusername', password='Password123!@#')
    return user

@pytest.fixture
def user_profile(user_login_data):
    return UserProfile.objects.create(user=user_login_data, height=180, weight=88, experience_in_months=16, age=27)

@pytest.fixture
def user_without_user_profile():
    return User.objects.create_user(username='Testusername2', password='Password123!@#')
