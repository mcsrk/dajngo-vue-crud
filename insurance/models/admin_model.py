from django.db import models

# Create your models here.


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_username = models.CharField(max_length=16)
    admin_password = models.CharField(max_length=16)
    admin_email = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.admin_name
