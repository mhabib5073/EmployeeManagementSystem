from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('employee', 'Employee')], default='employee')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
