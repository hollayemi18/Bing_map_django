from django.db import models

# Create your models here.


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)


def __str__(self):
    return (self.id)
