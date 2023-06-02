from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Works, Products
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class WorksApiView(APIView):
    def get(self, request):
        works = Works.objects.all().values()
        return Response({"Message": "List of works", "Work List": works})
    
    def post(self, request):
        Works.objects.create(id=request.data["id"],
                             title=request.data["title"],
                             description=request.data["description"],)
        works = Works.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"A new work has been introduced!", "Work": Works})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer