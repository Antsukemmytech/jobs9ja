from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import UserRegistrationForm
from resume.models import CV
from django.contrib import messages

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