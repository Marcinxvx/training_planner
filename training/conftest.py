import pytest
from django.contrib.auth.models import User
from training.models import WorkoutPlan, WorkoutSession, Exercise, ExerciseInSession
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

@pytest.fixture
def exercises(user, workout_plans, workout_sessions):
    exercises = []
    for i in range(10):
        exercises.append(Exercise.objects.create(user=user, name=f'Exercise {i}', description=f'Random description {i}'))
    return exercises

@pytest.fixture
def duplicated_exercises(user, workout_plans, workout_sessions):
    duplicated_exercises = []
    for i in range(2):
        for j in range(10):
            duplicated_exercises.append(Exercise.objects.create(user=user, name=f'Exercise {j}', description=f'Random description {j}'))
    return duplicated_exercises

@pytest.fixture
def exercises_in_session(user, workout_sessions, exercises):
    exercises_in_session = []
    for i in range(10):
        exercises_in_session.append(ExerciseInSession.objects.create(workout_session=workout_sessions[i], exercise=exercises[i], sets=i, repetitions=5 + i, weight=5 * i,))
    return exercises_in_session
