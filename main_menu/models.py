from django.db import models


class Slogan(models.Model):
    slogan = models.CharField(max_length=100)

    def __str__(self):
        return self.slogan

class Video(models.Model):
    video = models.URLField(max_length=200)

    def __str__(self):
        return self.video

class Product(models.Model):
    product = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', null=True)
    price = models.IntegerField(default=100, null=True)

    def __str__(self):
        return self.product


# Create your models here.
