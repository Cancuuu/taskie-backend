from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from taskieApp.models import Departments,Employees
from taskieApp.serializers import DepartmentSerializer,EmployeeSerializer


# Create your views here.

@csrf_exempt # le permite a otros dominios acceder a los api methods

def departmentApi(req, id=0):
    if req.method == 'GET': # En caso de que la peticion sea GET
        # obtenemos todos los objetos de Departments y los guardamos en variable departments
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif req.method == 'POST': # En caso de que la peticion sea POST
        department_data = JSONParser().parse(req)
        departments_serializer = DepartmentSerializer(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif req.method == 'PUT': # En caso de que la peticion sea PUT
        department_data = JSONParser().parse(req)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("actulizado!!!!!!!", safe= False)
        return JsonResponse("Fallo")
    elif req.method == 'DELETE': # En caso de que la peticion sea DELETE
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted succesfuly", safe = False)
         







