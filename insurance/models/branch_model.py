from django.db import models

from insurance.models import Company

# Create your models here.


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company, models.DO_NOTHING)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return self.name
