from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count():
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='slug_default')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title
