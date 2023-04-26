from django.contrib import admin

from insurance.models import Company, Branch, Employee, Admin

# Register your models here.
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(Admin)
