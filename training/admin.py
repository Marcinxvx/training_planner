from django.contrib import admin
from .models import WorkoutPlan, WorkoutSession, Exercise, ExerciseInSession
# Register your models here.

admin.site.register(WorkoutPlan)
admin.site.register(WorkoutSession)
admin.site.register(Exercise)
admin.site.register(ExerciseInSession)
