from rest_framework import serializers
from .models import Imagens

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ImageSerializer, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation