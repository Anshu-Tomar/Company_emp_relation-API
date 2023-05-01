from django.shortcuts import render
from rest_framework import viewsets 
from   rest_framework.response import Response
from .models import Company,Employee
from .serializers import companySerializer,employeeSerializer
from rest_framework.decorators import action
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = companySerializer

    @action(detail=True,methods=['get'])
    def employees(self, request,pk=None):
            company =Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializers = employeeSerializer(emps, many=True,context={'request':request})
            return Response(emps_serializers.data)
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
