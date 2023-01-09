# Generated by Django 4.1.4 on 2023-01-09 04:34

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='image',
            field=cloudinary.models.CloudinaryField(db_index=True, default=django.utils.timezone.now, max_length=255, verbose_name='Image'),
            preserve_default=False,
        ),
    ]
