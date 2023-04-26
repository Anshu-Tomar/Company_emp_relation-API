from django.shortcuts import render
from rest_framework import viewsets
from .models import Company
from .serializers import companySerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = companySerializer