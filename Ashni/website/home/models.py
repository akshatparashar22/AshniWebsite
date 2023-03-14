import email
from unicodedata import name
from django.db import models
from tables import Description

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    description = models.TextField()
    date = models.DateField()