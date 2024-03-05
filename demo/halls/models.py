# halls/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    departments = models.ManyToManyField(Department)
