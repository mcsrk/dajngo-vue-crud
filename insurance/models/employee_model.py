from django.db import models

from insurance.models import Branch
# Create your models here.


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=20)
    employee_uid = models.CharField(max_length=20)
    employee_email = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.branch_name
