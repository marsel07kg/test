from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    about_product = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=100)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.price}"


class Rewiews(models.Model):
    rewiews_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='rewiews_product'
    )
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=
                                        [MinValueValidator(1),
                                         MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars}-{self.rewiews_product}"


# Create your models here.
