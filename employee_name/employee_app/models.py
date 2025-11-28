from django.db import models
from django.contrib import admin
# Create your models here.
class Employee(models.Model):
    Employee_name = models.CharField(max_length=20,help_text="Enter Employee Name")
    age = models.IntegerField(help_text="Enter Employee Age")
    dob = models.DateField()
    Employee_id = models.IntegerField(help_text="Enter Employee ID")
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Employee_name', 'age', 'dob', 'Employee_id']
