from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from api.serializers import DiseaseSerializer, InputSerializer
from api.models import Disease, Input
from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

def diseaseList(request):
    if request.method == 'GET':
        queryset = Disease.objects.all()
        serializer = DiseaseSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

# def diseasedetail(request, pk):
#     if request.method == 'GET':
#         queryset = Disease.objects.all()

class DiseaseList(generics.ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    # def get(self, request, format=None):
    #     queryset = Disease.objects.all()
    #     serializer = DiseaseSerializer(queryset, many=True)
    #     return Response(serializer.data)

class DiseaseDetail(generics.RetrieveAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = DiseaseSerializer(snippet)
    #     return Response(serializer.data)

class InputViewSet(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)



