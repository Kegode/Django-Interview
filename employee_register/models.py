from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    file = models.FileField(default='SOME STRING')
    
