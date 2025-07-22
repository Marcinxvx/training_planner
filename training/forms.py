from django import forms
from training.models import WorkoutPlan


class CreateWorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'description']
        labels = {
            'name': 'Nazwa',
            'description': 'Opis',
        }
