from .models import Company, Employee
from rest_framework import serializers

class companySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Company
        fields="__all__"

     

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"