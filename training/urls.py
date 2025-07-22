from django.urls import path
from training import views

urlpatterns = [
    path('create_workout_plan', views.CreateWorkoutPlanView.as_view(), name='create_workout_plan'),

]
