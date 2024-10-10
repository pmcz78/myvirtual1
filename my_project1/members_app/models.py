from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.CharField(max_length=3)
  gender = models.CharField(max_length=6)


