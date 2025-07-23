from django.urls import path
from training import views

urlpatterns = [
    path('create_workout_plan', views.CreateWorkoutPlanView.as_view(), name='create_workout_plan'),
    path('update_workout_plan/<int:primary_key>', views.UpdateWorkoutPlanView.as_view(), name='update_workout_plan'),
    path('delete_plan/<int:primary_key>', views.DeleteWorkoutPlanView.as_view(), name='delete_workout_plan'),

]
