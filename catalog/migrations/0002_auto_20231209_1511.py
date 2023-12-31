# Generated by Django 5.0 on 2023-12-09 15:11

from django.db import migrations


def create_initial_games(apps, schema_editor):
    Game = apps.get_model('catalog', 'Game')
    games_data = [
        {'title': 'Super Mario Odyssey', 'description': 'Cool Mario Game with hat :))'},
        {'title': 'Animal Crossing: New Horizons', 'description': 'cool game with animals and they are crossing'},
        # Add more games as needed
    ]

    for data in games_data:
        Game.objects.create(**data)


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
    ]
