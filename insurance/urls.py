from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from insurance.views import CompanyView
from insurance.views import BranchView
from insurance.views import EmployeeView
from insurance.views import AdminView


router = routers.DefaultRouter()
router.register(r'admin', AdminView, 'admin')
router.register(r'companies', CompanyView, 'companies')
router.register(r'branches', BranchView, 'branches')
router.register(r'employees', EmployeeView, 'employees')


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Insurance API"))
]
