from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    experience_in_months = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    additional_info = models.TextField(blank=True)
    def __str__(self):
        return f"Profil użytkownika {self.user.username}"
