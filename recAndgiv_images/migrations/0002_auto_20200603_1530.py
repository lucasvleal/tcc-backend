# Generated by Django 3.0.3 on 2020-06-03 18:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recAndgiv_images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
