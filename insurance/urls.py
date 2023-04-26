from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from insurance.views import CompanyView
from insurance.views import BranchView


router = routers.DefaultRouter()
router.register(r'companies', CompanyView, 'companies')
router.register(r'branches', BranchView, 'branches')


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Insurance API"))
]
