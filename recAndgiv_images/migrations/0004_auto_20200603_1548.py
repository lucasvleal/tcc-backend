# Generated by Django 3.0.3 on 2020-06-03 18:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recAndgiv_images', '0003_auto_20200603_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagens',
            name='image_system',
            field=models.ImageField(null=True, upload_to='recAndgiv_images/first_images'),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
