from django.db import models

# Create your models here.

##Creamos un modelo departamento y le indicamos que necesitamos un id y un nombre
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=50)


##Creamos un modelo empleado y le indicamos que necesitamos id, nombre, departamento y fecha de inicio
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=150)
    Department = models.CharField(max_length=150)
    DateOfJoining = models.DateField()