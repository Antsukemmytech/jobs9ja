from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import UserRegistrationForm
from resume.models import CV
from django.contrib import messages
from company.models import Company

def register_applicant(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.save()
            CV.objects.create(user=user)
            messages.success(request, "Your account has been created successfully")
            return redirect('login')
        else:
            messages.warning("Something went wrong")
            return redirect('users/register_applicant.html')
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register_applicant.html', {'form': form})
    
    # Recruiter Registration

def register_recruiter(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_recruiter = True
            user.save()
            Company.objects.create(user=user)
            messages.success(request, "Your account has been created successfully")
            return redirect('login')
        else:
            messages.warning("Something went wrong")
            return redirect('users/register_recruiter.html')
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register_recruiter.html', {'form': form})


# login
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        if request.user.is_applicant:
            return redirect('applicant-dashboard')
        elif request.user.is_recruiter:
            return redirect('recruiter-dashboard')
    else:
        return redirect('login')
    

    # logout
def logout_user(request):
    logout(request)
    messages.success('Logout Successful')
    return redirect('login')

    
   