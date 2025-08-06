from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Min
from django.shortcuts import render, redirect
from django.views import View
from django import forms
from training.forms import CreateWorkoutPlanForm, CreateWorkoutSessionForm, CreateWorkoutSessionForPlanForm, CreateExerciseForm
from training.models import WorkoutPlan, WorkoutSession, Exercise



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
            return redirect('create_workout_plan')
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
            return redirect('create_workout_session')
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

class CreateExerciseView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('search', '')
        exercises = Exercise.objects.filter(user=request.user).order_by('name')
        if query:
            exercises = exercises.filter(name__icontains=query)
        form = CreateExerciseForm()
        return render(request, 'training/create_exercise.html', {'form': form, 'exercises': exercises, 'query': query})
    def post(self, request):
        query = request.GET.get('search', '')
        exercises = Exercise.objects.filter(user=request.user).order_by('name')
        form = CreateExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect('create_exercise')
        return render(request, 'training/create_exercise.html', {'form': form, 'exercises': exercises, 'query': query})

class UpdateExerciseView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        exercise = Exercise.objects.get(pk=primary_key, user=request.user)
        form = CreateExerciseForm(instance=exercise)
        return render(request, 'training/update_exercise.html', {'form': form, 'exercise': exercise})
    def post(self, request, primary_key):
        exercise = Exercise.objects.get(pk=primary_key, user=request.user)
        form = CreateExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('create_exercise')
        return render(request, 'training/update_exercise.html', {'form': form, 'exercise': exercise})

class DeleteExerciseView(LoginRequiredMixin, View):
    def get(self, request, primary_key):
        exercise = Exercise.objects.get(pk=primary_key, user=request.user)
        return render(request,'training/delete_exercise.html', {'exercise': exercise})
    def post(self, request, primary_key):
        if request.POST.get('operation') == 'Yes':
            exercise = Exercise.objects.get(pk=primary_key, user=request.user)
            exercise.delete()
        return redirect('create_exercise')

class PublicExerciseListView(View):
    def get(self, request):
        query = request.GET.get('search', '')
        exercises = Exercise.objects.none()
        if request.user.is_authenticated:
            other_users_exercises = Exercise.objects.exclude(user=request.user)
            user_exercise_names = Exercise.objects.filter(user=request.user).values_list('name', flat=True)
            other_users_exercises = other_users_exercises.exclude(name__in=user_exercise_names)
            unique_ids = (other_users_exercises.values('name').annotate(first_id=Min('id')).values_list('first_id', flat=True))
            exercises = Exercise.objects.filter(id__in=unique_ids)
        else:
            unique_ids = Exercise.objects.values('name').annotate(first_id=Min('id')).values_list('first_id', flat=True)
            exercises = Exercise.objects.filter(id__in=unique_ids)
        if query:
            exercises = exercises.filter(name__icontains=query)
        return render(request, 'training/public_exercise_list.html', {'exercises': exercises,'query': query})

class CopyExerciseView(LoginRequiredMixin, View):
    def post(self, request, primary_key):
        original = Exercise.objects.get(pk=primary_key)
        already_exists = Exercise.objects.filter(user=request.user, name=original.name, description=original.description).exists()
        if not already_exists:
            Exercise.objects.create(name=original.name, description=original.description, user=request.user)
        return redirect('public_exercise_list')
