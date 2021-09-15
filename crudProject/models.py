from django.db import models


class crudEmployee(models.Model):
    ename = models.CharField(max_length=100)
    eaddress = models.CharField(max_length=100)
    age = models.IntegerField()
    egender = models.CharField(max_length=1)