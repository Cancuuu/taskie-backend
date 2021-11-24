### serializers

from rest_framework import serializers
from taskieApp.models import Departments,Employees

## los serializers permiten convertir una estructura del orm de django a un json
## para luego retornarla en un response en views.py

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName') #Indicamos cuales van a ser los campos dentro de 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: # incluimos la clase "Meta" para indicarle que le vamos a pasar un modelo y no campos en especifico
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining')
