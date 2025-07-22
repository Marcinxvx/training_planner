from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from training.forms import CreateWorkoutPlanForm


# Create your views here.

class CreateWorkoutPlanView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateWorkoutPlanForm()
        return render(request, 'training/create_workout_plan.html', {'form': form, 'button_text': 'Utwórz'})
    def post(self, request):
        form = CreateWorkoutPlanForm(request.POST)
        if form.is_valid():
            workout_plan = form.save(commit=False)
            workout_plan.user = request.user
            form.save()
            return redirect('home')
        return render(request, 'training/create_workout_plan.html', {'form': form,  'button_text': 'Utwórz'})
