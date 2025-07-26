from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from training.forms import CreateWorkoutPlanForm
from training.models import WorkoutPlan


# Create your views here.

class CreateWorkoutPlanView(LoginRequiredMixin, View):
    def get(self, request):
        workout_plans = WorkoutPlan.objects.filter(user=request.user)
        form = CreateWorkoutPlanForm()
        return render(request, 'training/create_workout_plan.html', {'form': form, 'workout_plans': workout_plans})
    def post(self, request):
        form = CreateWorkoutPlanForm(request.POST)
        if form.is_valid():
            workout_plan = form.save(commit=False)
            workout_plan.user = request.user
            workout_plan.save()
            return redirect('home')
        return render(request, 'training/create_workout_plan.html', {'form': form})

class UpdateWorkoutPlanView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
        form = CreateWorkoutPlanForm(instance=workout_plan)
        return render(request, 'training/update_workout_plan.html', {'form': form, 'workout_plan': workout_plan} )
    def post(self, request, primary_key):
        workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
        form = CreateWorkoutPlanForm(request.POST, instance=workout_plan)
        if form.is_valid():
            form.save()
            return redirect('create_workout_plan')
        return render(request, 'training/update_workout_plan.html', {'form': form, 'workout_plan': workout_plan} )

class DeleteWorkoutPlanView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
        return render(request, 'training/delete_workout_plan.html', {'workout_plan': workout_plan})
    def post(self, request, primary_key):
        if request.POST.get('operation') == 'Yes':
            workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
            workout_plan.delete()
        return redirect('create_workout_plan')
