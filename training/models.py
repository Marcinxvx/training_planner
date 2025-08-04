from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercises = models.ManyToManyField('Exercise', through='ExerciseInSession')
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.IntegerField(choices=[(0, "Incomplete"), (1, "Complete")], default=0)
    note = models.TextField(blank=True)
    def __str__(self):
        return f"Plan: {self.workout_plan.name}, Workout session: {self.name}, Date: {self.date}, Status: {self.get_status_display()}"

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Exercise: {self.name}"

class ExerciseInSession(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField()
    def __str__(self):
        return f"Exercise: {self.exercise.name}, Sets: {self.sets}, Reps: {self.repetitions}, Weight: {self.weight}"
