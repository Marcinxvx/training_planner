import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from accounts.models import UserProfile


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

@pytest.mark.django_db
def test_create_user_profile_view_profile_exists_get(user_login_data, user_profile):
    c = Client()
    c.force_login(user_login_data)
    response = c.get(reverse('create_user_profile'))
    assert response.status_code == 200
    assert response.context['profile_exists'] is True
    assert response.context['user_profile'].id == user_profile.id
    assert UserProfile.objects.count() == 1

@pytest.mark.django_db
def test_create_user_profile_view_post_success(user_without_user_profile):
    c = Client()
    c.force_login(user_without_user_profile)
    data = {'height': 165, 'weight': 100, 'experience_in_months': 38, 'age': 42}
    response = c.post(reverse('create_user_profile'), data)
    assert response.status_code == 302
    assert UserProfile.objects.filter(user=user_without_user_profile, height=165, weight=100, experience_in_months=38, age=42).exists()
    assert UserProfile.objects.count() == 1

@pytest.mark.django_db
def test_update_user_profile_view_get(user_login_data, user_profile):
    c = Client()
    c.force_login(user_login_data)
    response = c.get(reverse('update_user_profile'))
    assert response.status_code == 200
    assert response.context['user_profile'].id == user_profile.id
    assert response.context['form'].initial['height'] == user_profile.height
    assert response.context['form'].initial['weight'] == user_profile.weight
    assert response.context['form'].initial['experience_in_months'] == user_profile.experience_in_months
    assert response.context['form'].initial['age'] == user_profile.age

@pytest.mark.django_db
def test_update_user_profile_view_post_success(user_login_data, user_profile):
    c = Client()
    c.force_login(user_login_data)
    data = {'height': 150, 'weight': 200, 'experience_in_months': 1, 'age': 20}
    response = c.post(reverse('update_user_profile'), data)
    assert response.status_code == 302
    user_profile.refresh_from_db()
    assert data['height'] == user_profile.height
    assert data['weight'] == user_profile.weight
    assert data['experience_in_months'] == user_profile.experience_in_months
    assert data['age'] == user_profile.age
    assert UserProfile.objects.count() == 1

@pytest.mark.django_db
def test_delete_user_profile_view_get(user_login_data, user_profile):
    c = Client()
    c.force_login(user_login_data)
    response = c.get(reverse('delete_user_profile'))
    assert response.status_code == 200
    assert response.context['user_profile'].id == user_profile.id

@pytest.mark.django_db
def test_delete_user_profile_view_post_success(user_login_data, user_profile):
    c = Client()
    c.force_login(user_login_data)
    data = {'operation': 'Yes'}
    response = c.post(reverse('delete_user_profile'), data)
    assert response.status_code == 302
    assert not UserProfile.objects.filter(user=user_login_data).exists()
    assert UserProfile.objects.count() == 0
