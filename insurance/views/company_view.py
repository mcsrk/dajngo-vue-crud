from rest_framework import viewsets

from insurance.serializers import CompanySerializer

from insurance.models import Company

# Create your views here.


class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
