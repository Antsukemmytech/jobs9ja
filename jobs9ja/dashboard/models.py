# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class User(AbstractUser):
    
#     pass

# class Applicant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.TextField()
    

# class Recruiter(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=255)
#     # Add other fields as needed

# class JobPosting(models.Model):
#     recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     # Add other fields as needed

# class Application(models.Model):
#     applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
#     job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
#     status = models.CharField(max_length=255, default='submitted')
#     # Add other fields as needed

