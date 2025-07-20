from django.urls import path
from accounts import views
from .views import RegisterUserView, LoginUserView, LogoutUserView
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),

]
