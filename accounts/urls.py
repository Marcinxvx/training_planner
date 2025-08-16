from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('create_user_profile/', views.CreateUserProfileView.as_view(), name='create_user_profile'),
    path('update_user_profile/', views.UpdateUserProfileView.as_view(), name='update_user_profile'),
    path('delete_user_profile/', views.DeleteUserProfileView.as_view(), name='delete_user_profile'),
    path('training_advice/', views.TrainingAdviceView.as_view(), name='training_advice'),

]
