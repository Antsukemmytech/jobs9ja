from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True) 
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    founded = models.DateField(blank=True, null=True)
    industry= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CompanyIndustry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# class CompanySize(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

# class CompanyType(models.Model):
#     # name = models.CharField(max_length=100)
#     # description = models.TextField(blank=True)

#     # def __str__(self):
    #     return self.name

class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.company.name} - {self.city}'

