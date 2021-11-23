from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from taskieApp.models import Departments,Employees
from taskieApp.serializers import DepartmentSerializer,EmployeeSerializer


# Create your views here.

@csrf_exempt

def departmentApi(req, id=0):
    if req.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif req.method == 'POST':
        department_data = JSONParser().parse(req)
        departments_serializer = DepartmentSerializer(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif req.method == 'PUT':
        department_data = JSONParser().parse(req)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("actulizado!!!!!!!", safe= False)
        return JsonResponse("Fallo")
    elif req.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted succesfuly", safe = False)
         







