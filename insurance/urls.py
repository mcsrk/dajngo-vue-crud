from django.urls import path, include
from rest_framework import routers

from insurance import views

router = routers.DefaultRouter()
router.register(r'companies',views.CompanyView, 'companies')


urlpatterns=[
    path("api/v1/", include(router.urls))
]

