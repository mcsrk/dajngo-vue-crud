from django.db import models

# Create your models here.


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=50)
    branch_city = models.CharField(max_length=50)
    branch_phone = models.CharField(max_length=20)
    company = models.ForeignKey('Company', models.DO_NOTHING)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return self.company_name
