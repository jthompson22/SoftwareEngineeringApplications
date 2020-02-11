Learn more or give us feedback
from django.db import models

# Create your models here.


class WaterQuantity(models.Model):
    river_name = models.CharField(max_length=100)
    enteree = models.CharField(max_length=100)