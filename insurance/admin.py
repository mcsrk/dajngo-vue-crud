from django.contrib import admin

from insurance.models import Company
from insurance.models import Branch

# Register your models here.
admin.site.register(Company)
admin.site.register(Branch)
