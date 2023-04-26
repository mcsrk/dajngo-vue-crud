from rest_framework import viewsets

from insurance.serializers import AdminSerializer

from insurance.models import Admin

# Create your views here.


class AdminView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()
