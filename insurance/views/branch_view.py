from rest_framework import viewsets

from insurance.serializers import BranchSerializer

from insurance.models import Branch

# Create your views here.


class BranchView(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
