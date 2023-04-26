from .models import Company
from rest_framework import serializers

class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"