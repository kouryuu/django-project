from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    passw = models.CharField(max_length=200)


# Create your models here.
