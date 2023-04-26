from django.db import models

from insurance.models import Branch
# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    uid = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name
