from rest_framework import viewsets

from insurance.serializers import EmployeeSerializer

from insurance.models import Employee

# Create your views here.


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
