from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from enum import Enum


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
    game_type = models.CharField(max_length=40, choices=[(tag.value, tag.name) for tag in GameType], default=GameType.TMP.value)
    carrier = models.CharField(max_length=40, default="null")
    cover = models.ImageField(upload_to='images/', null=True, blank=True, default='null')


# Signal to delete the image file when a model instance is deleted
@receiver(pre_delete, sender=Game)
def delete_image_file(sender, instance, **kwargs):
    if instance.cover:
        instance.cover.delete(save=False)
