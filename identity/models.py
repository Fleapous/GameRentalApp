from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, default='null')
    city = models.CharField(max_length=100, default='null')
    state = models.CharField(max_length=100, null='null')
    zip_code = models.CharField(max_length=10, null='null')

    def __str__(self):
        return f"{self.user.username}'s Address"
