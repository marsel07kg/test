from django.db import models

class Contact(models.Model):
    number = models.IntegerField()
    street = models.TextField()

    def __str__(self):
        return f"{self.number} - {self.street}"
# Create your models here.
