from django.db import models
from insurance.models import Admin

# Create your models here.


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    admin = models.ForeignKey(Admin, models.DO_NOTHING)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name
