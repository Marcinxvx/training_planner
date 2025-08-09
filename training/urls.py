from django.urls import path
from training import views

urlpatterns = [
    path('create_workout_plan', views.CreateWorkoutPlanView.as_view(), name='create_workout_plan'),
    path('update_workout_plan/<int:primary_key>', views.UpdateWorkoutPlanView.as_view(), name='update_workout_plan'),
    path('delete_plan/<int:primary_key>', views.DeleteWorkoutPlanView.as_view(), name='delete_workout_plan'),
    path('create_workout_session', views.CreateWorkoutSessionView.as_view(), name='create_workout_session'),
    path('update_workout_session/<int:primary_key>', views.UpdateWorkoutSessionView.as_view(), name='update_workout_session'),
    path('delete_session/<int:primary_key>', views.DeleteWorkoutSessionView.as_view(), name='delete_workout_session'),
    path('workout_plan_detail/<int:primary_key>', views.WorkoutPlanDetailView.as_view(), name='workout_plan_detail'),
    path('create_exercise', views.CreateExerciseView.as_view(), name='create_exercise'),
    path('update_exercise/<int:primary_key>', views.UpdateExerciseView.as_view(), name='update_exercise'),
    path('delete_exercise/<int:primary_key>', views.DeleteExerciseView.as_view(), name='delete_exercise'),
    path('public_exercise_list/', views.PublicExerciseListView.as_view(), name='public_exercise_list'),
    path('public_exercise_list/copy/<int:primary_key>/', views.CopyExerciseView.as_view(), name='copy_exercise'),
    path('create_exercise_in_session/<int:primary_key>/', views.CreateExerciseInSessionView.as_view(), name='create_exercise_in_session'),
    path('update_exercise_in_session/<int:primary_key>', views.UpdateExerciseInSessionView.as_view(), name='update_exercise_in_session'),
    path('delete_exercise_in_session/<int:primary_key>', views.DeleteExerciseInSessionView.as_view(), name='delete_exercise_in_session'),
    path('workout_plan/<int:primary_key>/pdf', views.GenerateWorkoutPlanPdfView.as_view(), name='generate_workout_plan_pdf'),

]
