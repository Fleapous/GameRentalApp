# Generated by Django 5.0 on 2024-01-07 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0001_initial'),
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identity.address'),
        ),
    ]
