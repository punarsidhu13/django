from django.db import models

# Create your models here.

class Amazon(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=150)
    quantity = models.IntegerField(max_length=100)


