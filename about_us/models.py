from django.db import models
class Shop(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    shop = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.shop
# Create your models here.
