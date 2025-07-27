from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django import forms
from training.forms import CreateWorkoutPlanForm, CreateWorkoutSessionForm, CreateWorkoutSessionForPlanForm
from training.models import WorkoutPlan, WorkoutSession


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

class CreateWorkoutSessionView(LoginRequiredMixin, View):
    def get(self, request):
        workout_sessions = WorkoutSession.objects.filter(workout_plan__user=request.user).order_by('date')
        form = CreateWorkoutSessionForm()
        form.fields['workout_plan'].queryset = WorkoutPlan.objects.filter(user=request.user)
        return render(request, 'training/create_workout_session.html', {'form': form, 'workout_sessions': workout_sessions})
    def post(self, request):
        workout_sessions = WorkoutSession.objects.filter(workout_plan__user=request.user).order_by('date')
        form = CreateWorkoutSessionForm(request.POST)
        form.fields['workout_plan'].queryset = WorkoutPlan.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'training/create_workout_session.html', {'form': form, 'workout_sessions': workout_sessions})

class UpdateWorkoutSessionView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        workout_session = WorkoutSession.objects.get(pk=primary_key, workout_plan__user=request.user)
        form = CreateWorkoutSessionForm(instance=workout_session)
        form.fields['workout_plan'].queryset = WorkoutPlan.objects.filter(user=request.user)
        return render(request, 'training/update_workout_session.html', {'form': form, 'workout_session': workout_session})
    def post(self, request, primary_key):
        workout_session = WorkoutSession.objects.get(pk=primary_key, workout_plan__user=request.user)
        form = CreateWorkoutSessionForm(request.POST, instance=workout_session)
        form.fields['workout_plan'].queryset =WorkoutPlan.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            return redirect ('create_workout_session')
        return render(request, 'training/update_workout_session.html', {'form': form, 'workout_session': workout_session})

class DeleteWorkoutSessionView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        workout_session = WorkoutSession.objects.get(pk=primary_key, workout_plan__user=request.user)
        return render(request, 'training/delete_workout_session.html', {'workout_session': workout_session})
    def post(self, request, primary_key):
        if request.POST.get('operation') == 'Yes':
            workout_session = WorkoutSession.objects.get(pk=primary_key, workout_plan__user=request.user)
            workout_session.delete()
        return redirect('create_workout_session')

class WorkoutPlanDetailView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        workout_sessions = WorkoutSession.objects.filter(workout_plan__pk=primary_key, workout_plan__user=request.user).order_by('date')
        workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
        form = CreateWorkoutSessionForPlanForm()
        return render(request, 'training/workout_plan_detail.html', {'form': form, 'workout_sessions': workout_sessions, 'workout_plan': workout_plan})
    def post(self, request, primary_key):
        workout_sessions = WorkoutSession.objects.filter(workout_plan__pk=primary_key, workout_plan__user=request.user).order_by('date')
        workout_plan = WorkoutPlan.objects.get(pk=primary_key, user=request.user)
        form = CreateWorkoutSessionForPlanForm(request.POST)
        if form.is_valid():
            workout_session = form.save(commit=False)
            workout_session.workout_plan = workout_plan
            workout_session.save()
            return redirect('create_workout_plan')
        return render(request, 'training/workout_plan_detail.html', {'form': form, 'workout_sessions': workout_sessions, 'workout_plan': workout_plan})
