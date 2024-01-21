from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from enum import Enum
from django.contrib.auth.models import User


# Create your models here.

class GameType(Enum):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    STRATEGY = 'Strategy'
    RPG = 'Role-Playing'
    PLATFORMER2D = '2D Platformer'
    Platformer3D = '3D platformer'
    TMP = 'not assigned'


class Game(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    platform = models.CharField(max_length=60, default="null")
    game_type = models.CharField(max_length=40, choices=[(tag.value, tag.name) for tag in GameType],
                                 default=GameType.TMP.value)
    carrier = models.CharField(max_length=40, default="null")
    cover = models.ImageField(upload_to='images/', null=True, blank=True, default='null')


@receiver(pre_delete, sender=Game)
def delete_image_file(sender, instance, **kwargs):
    if instance.cover:
        instance.cover.delete(save=False)


class Comment(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
