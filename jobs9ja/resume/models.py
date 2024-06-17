from django.db import models
from users.models import User


class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    key_responsibilities = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.position} at {self.company}"

    