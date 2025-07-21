import pytest
from django.contrib.auth.models import User

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
