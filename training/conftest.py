import pytest
from django.contrib.auth.models import User
from training.models import WorkoutPlan

@pytest.fixture
def user():
    return User.objects.create_user(username='TestUser', password='Password123!@#')

@pytest.fixture
def workout_plans(user):
    plans = []
    for i in range(10):
        plans.append(WorkoutPlan.objects.create(user=user, name=f'Workout Plan {i}', description=f'Random description {i}'))
    return plans

