from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=8)
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=8)
