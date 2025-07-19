from django.urls import path
from accounts import views
from .views import RegisterUserView
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),

]
