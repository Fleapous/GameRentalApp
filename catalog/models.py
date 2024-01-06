from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)


# Signal to delete the image file when a model instance is deleted
@receiver(pre_delete, sender=Game)
def delete_image_file(sender, instance, **kwargs):
    if instance.cover:
        instance.cover.delete(save=False)
