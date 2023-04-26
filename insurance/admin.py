from django.contrib import admin

from insurance.models import Company
from insurance.models import Branch
from insurance.models import Employee

# Register your models here.
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Employee)
