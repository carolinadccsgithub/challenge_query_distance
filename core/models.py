from django.db import models

# Create your models here.
class QueryDistance(models.Model):
    source_address = models.CharField('Source', max_length=1000)
    destination_address = models.CharField('Destination', max_length=1000)
    distance = models.CharField('Distance', max_length=1000)