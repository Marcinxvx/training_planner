from django import forms
from training.models import WorkoutPlan, WorkoutSession, Exercise, ExerciseInSession


class CreateWorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'description']
        labels = {
            'name': 'Nazwa',
            'description': 'Opis',
        }

class CreateWorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['workout_plan', 'name', 'date', 'status', 'note']
        labels = {
            'workout_plan': 'Plan treningowy',
            'name': 'Nazwa',
            'date': 'Data',
            'status': 'Status',
            'note': 'Uwagi',
        }
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.RadioSelect(),
        }

class CreateWorkoutSessionForPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['name', 'date', 'status', 'note']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.RadioSelect(),
        }

class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description']
        labels = {
            'name': 'Nazwa',
            'description': 'Opis',
        }
class CreateExerciseInSessionForm(forms.ModelForm):
    class Meta:
        model = ExerciseInSession
        fields = ['exercise', 'sets', 'repetitions', 'weight']
        labels = {
            'exercise': 'Ćwiczenie',
            'sets': 'Serie',
            'repetitions': 'Powtórzenia',
            'weight': 'Ciężar',
        }

class UpdateExerciseInSessionForm(forms.ModelForm):
    class Meta:
        model = ExerciseInSession
        fields = ['sets', 'repetitions', 'weight']
        labels = {
            'sets': 'Serie',
            'repetitions': 'Powtórzenia',
            'weight': 'Ciężar',
        }
