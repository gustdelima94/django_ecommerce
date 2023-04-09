from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    desription = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)