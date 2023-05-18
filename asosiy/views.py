import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializer import *
from .models import *


class BolimSerializerAPI(APIView):
    def get(self, request):
        bolim_name = request.query_params.get('qidirish', '')
        bolim = self.get_queryset(bolim_name)
        serializer = BolimSerializer(bolim, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self, bolim_name=''):
        if bolim_name == '':
            natija = Bolim.objects.all()
        else:
            natija = Bolim.objects.filter(nom__contains=bolim_name)
        return natija

class BolimgaTegishliSozlar(APIView):
    def get(self,request,pk):
        sozlar=Sozlar.objects.filter(bolim_fk__id=pk)
        serializer=SozlarSerializer(sozlar,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)