from rest_framework import serializers
from .models import Product, Genre


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'get_absolute_url', 'price', 'get_image', 'get_image_resized', 'get_audio_file']


class GenreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'get_absolute_url', 'products']