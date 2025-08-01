import pytest
from django.contrib.auth.models import User
from training.models import WorkoutPlan, WorkoutSession
from django.utils.timezone import now
from datetime import datetime,timezone, timedelta

@pytest.fixture
def user():
    return User.objects.create_user(username='TestUser', password='Password123!@#')

@pytest.fixture
def workout_plans(user):
    plans = []
    for i in range(10):
        plans.append(WorkoutPlan.objects.create(user=user, name=f'Workout Plan {i}', description=f'Random description {i}'))
    return plans

@pytest.fixture
def workout_sessions(user, workout_plans):
    sessions = []
    for i in range(10):
        sessions.append(WorkoutSession.objects.create(workout_plan=workout_plans[i], name=f'Workout Session {i}', date=datetime.now(timezone.utc)+timedelta(days=i), status=i % 2, note=f'Random note {i}'))
    return sessions
