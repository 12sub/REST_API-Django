from rest_framework import serializers
from .models import Works, Products

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"