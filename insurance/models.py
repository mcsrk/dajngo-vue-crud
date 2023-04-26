from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=50)

    class Meta:
        db_table = 'company'

        
    def __str__(self):
        return self.company_name