import pytest
from django.test import Client
from django.urls import reverse
from training.models import WorkoutPlan


# Create your tests here.

@pytest.mark.django_db
def test_create_workout_plan_view_get(user, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('create_workout_plan'))
    assert response.status_code == 200
    assert response.context['workout_plans'].count() == len(workout_plans)
    for workout_plan in workout_plans:
        assert workout_plan in response.context['workout_plans']

@pytest.mark.django_db
def test_create_workout_plan_view_post_success(user):
    c = Client()
    c.force_login(user)
    data = {'name': 'Test name', 'description': 'Test description'}
    response = c.post(reverse('create_workout_plan'), data)
    assert response.status_code == 302
    assert WorkoutPlan.objects.filter(user=user, name=data['name'], description=data['description']).exists()

@pytest.mark.django_db
def test_update_workout_plan_view_get(user, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('update_workout_plan', kwargs={'primary_key': workout_plans[0].id}))
    assert response.status_code == 200
    assert response.context['workout_plan'].id == workout_plans[0].id
    assert response.context['form'].initial['name'] == workout_plans[0].name
    assert response.context['form'].initial['description'] == workout_plans[0].description

@pytest.mark.django_db
def test_update_workout_plan_view_post_success(user, workout_plans):
    c = Client()
    c.force_login(user)
    data = {'name': 'Other name', 'description': 'Other description'}
    response = c.post(reverse('update_workout_plan', kwargs={'primary_key': workout_plans[0].id}), data)
    assert response.status_code == 302
    workout_plans[0].refresh_from_db()
    assert data['name'] == workout_plans[0].name
    assert data['description'] == workout_plans[0].description

@pytest.mark.django_db
def test_delete_workout_plan_view_get(user, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('delete_workout_plan', kwargs={'primary_key': workout_plans[0].id}))
    assert response.status_code == 200
    assert response.context['workout_plan'].id == workout_plans[0].id

@pytest.mark.django_db
def test_delete_workout_plan_view_post_success(user, workout_plans):
    c = Client()
    c.force_login(user)
    data = {'operation': 'Yes'}
    response = c.post(reverse('delete_workout_plan', kwargs={'primary_key': workout_plans[0].id}), data)
    assert response.status_code == 302
    assert not WorkoutPlan.objects.filter(user=user, id=workout_plans[0].id).exists()

