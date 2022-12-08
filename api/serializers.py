from rest_framework import serializers
from api.models import Disease, Input

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = "__all__"

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = "__all__"