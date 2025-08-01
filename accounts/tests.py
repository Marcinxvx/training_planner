import pytest
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

@pytest.mark.django_db
def test_register_user_success(client, users_to_register_success):
    for username, password in users_to_register_success:
        data = {
            'username': username,
            'password1': password,
            'password2': password,
        }
        response = client.post(reverse('register'), data)
        assert response.status_code == 302
        assert User.objects.filter(username=username).exists()

@pytest.mark.django_db
def test_register_user_fail(client):
    data = {
        'username': 'Testusername',
        'password1': 'Password123!@#',
        'password2': 'OtherPassword123!@#',
    }
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert not User.objects.filter(username='Testusername').exists()

@pytest.mark.django_db
def test_login_user_success(client, user_login_data):
    data = {
        'username': 'Testusername',
        'password': 'Password123!@#',
    }
    response = client.post(reverse('login'), data)
    assert response.status_code == 302
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_login_user_fail(client, user_login_data):
    data = {
        'username': 'Testusername',
        'password': 'WrongPassword123!@#',
    }
    response = client.post(reverse('login'), data)
    assert response.status_code == 200
    assert '_auth_user_id' not in client.session

@pytest.mark.django_db
def test_logout_user(client, user_login_data):
    client.login(username=user_login_data.username, password='Password123!@#')
    assert '_auth_user_id' in client.session
    data = {
        'operation': 'Yes'
    }
    response = client.post(reverse('logout'), data)
    assert response.status_code == 302
    assert '_auth_user_id' not in client.session
