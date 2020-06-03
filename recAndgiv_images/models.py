from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Imagens(models.Model):
    image = CloudinaryField('image')
    image_system = models.ImageField(null=True, upload_to='recAndgiv_images/first_images')