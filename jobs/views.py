from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Application
from django.contrib import messages

def home(request):
    jobs = Job.objects.all().order_by('-posted_date')
    return render(request, 'index.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        Application.objects.create(job=job, applicant=request.user, cover_letter=cover_letter)
        messages.success(request, 'Application submitted successfully!')
        return redirect('job_detail', job_id=job.id)
    return redirect('job_detail', job_id=job.id)

@login_required
def job_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            description=description,
            employer=request.user
        )
        messages.success(request, 'Job posted successfully!')
        return redirect('home')
    return render(request, 'job_create.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})