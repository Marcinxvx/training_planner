import pytest
from django.test import Client
from django.urls import reverse
from training.models import WorkoutPlan, WorkoutSession
from datetime import datetime, timezone

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

@pytest.mark.django_db
def test_create_workout_session_view_get(user, workout_sessions, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('create_workout_session'))
    assert response.status_code == 200
    assert response.context['workout_sessions'].count() == len(workout_sessions)
    assert list(response.context['form'].fields['workout_plan'].queryset) == workout_plans
    for workout_session in workout_sessions:
        assert workout_session in response.context['workout_sessions']
        assert workout_session.workout_plan.user == user

@pytest.mark.django_db
def test_create_workout_session_view_post_success(user, workout_sessions):
    c = Client()
    c.force_login(user)
    data = {'workout_plan': workout_sessions[0].workout_plan.id, 'name': 'Test name', 'date': '2025-07-27 13:00:00', 'status': 0, 'note': 'Test note'}
    response = c.post(reverse('create_workout_session'), data)
    assert response.status_code == 302
    assert WorkoutSession.objects.filter(workout_plan__user=user, name=data['name'], date=data['date'], status=data['status'], note=data['note']).exists()

@pytest.mark.django_db
def test_update_workout_session_view_get(user, workout_sessions, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('update_workout_session', kwargs={'primary_key': workout_sessions[0].id}))
    assert response.status_code == 200
    assert response.context['workout_session'].id == workout_sessions[0].id
    assert response.context['form'].initial['name'] == workout_sessions[0].name
    assert response.context['form'].initial['date'] == workout_sessions[0].date
    assert response.context['form'].initial['status'] == workout_sessions[0].status
    assert response.context['form'].initial['note'] == workout_sessions[0].note
    assert response.context['form'].initial['workout_plan'] == workout_sessions[0].workout_plan_id

@pytest.mark.django_db
def test_update_workout_session_view_post_success(user, workout_sessions, workout_plans):
    c = Client()
    c.force_login(user)
    date = {'workout_plan': workout_sessions[1].workout_plan_id, 'name': 'Other name', 'date': datetime(2025, 8, 30, 10, 30, tzinfo=timezone.utc), 'status': 1, 'note': 'Other note'}
    response = c.post(reverse('update_workout_session', kwargs={'primary_key': workout_sessions[0].id}), date)
    assert response.status_code == 302
    workout_sessions[0].refresh_from_db()
    assert date['workout_plan'] == workout_sessions[0].workout_plan.id
    assert date['name'] == workout_sessions[0].name
    assert date['date'] == workout_sessions[0].date
    assert date['status'] == workout_sessions[0].status
    assert date['note'] == workout_sessions[0].note

@pytest.mark.django_db
def test_delete_workout_session_view_get(user, workout_sessions, workout_plans):
    c = Client()
    c.force_login(user)
    response = c.get(reverse('delete_workout_session', kwargs={'primary_key': workout_sessions[0].id}))
    assert response.status_code == 200
    assert response.context['workout_session'].id == workout_sessions[0].id

@pytest.mark.django_db
def test_delete_workout_session_view_post_success(user, workout_sessions, workout_plans):
    c = Client()
    c.force_login(user)
    date = {'operation': 'Yes'}
    response = c.post(reverse('delete_workout_session', kwargs={'primary_key': workout_sessions[0].id}), date)
    assert response.status_code == 302
    assert not WorkoutSession.objects.filter(id=workout_sessions[0].id, workout_plan__user=user).exists()
