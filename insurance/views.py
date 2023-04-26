from rest_framework import viewsets

from .serializer import CompanySerializer

from .models import  Company

# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
 