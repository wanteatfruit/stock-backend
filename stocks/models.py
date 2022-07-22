from django.db import models
from sqlalchemy import true

# Create your models here.


class A(models.Model):
    current_date = models.CharField(max_length=10, primary_key=true)
    price = models.FloatField(null=true)


class B(models.Model):


    current_date = models.CharField(max_length=10, primary_key=true)
    price = models.FloatField(null=true)


class C(models.Model):


    current_date = models.CharField(max_length=10, primary_key=true)
    price = models.FloatField(null=true)
