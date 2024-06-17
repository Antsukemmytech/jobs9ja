from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    
    has_cv = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)


class Recuriters(models.Model):
    pass


class Applicant (models.Model):
    pass