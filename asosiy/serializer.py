from rest_framework import serializers
from .models import *
class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bolim
        fields='__all__'
class SozlarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sozlar
        fields='__all__'