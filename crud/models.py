from django.db import models

# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    country = models.CharField(max_length=100)