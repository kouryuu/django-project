from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    name3 = models.CharField(max_length=200)
