from django.db import models
from django.contrib.auth.models import User
from catalog.models import Game
from identity.models import Address


# Create your models here.
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    get_digital_code_only = models.BooleanField(default=False)
    delivery_method = models.CharField(max_length=20, choices=[
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('next_day', 'Next Day'),
    ], null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Rental - {self.game.title}"

    