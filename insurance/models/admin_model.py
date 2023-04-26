from django.db import models

# Create your models here.


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.name
