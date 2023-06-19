from io import BytesIO
from PIL import Image
import os

from django.core.files import File
from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    genre = models.ForeignKey(Genre, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_resized = models.ImageField(upload_to='uploads/', blank=True, null=True)
    audio_file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_audio_file(self):
        return 'http://127.0.0.1:8000' + self.audio_file.url
    
    def get_image_resized(self):
        if self.image_resized:
            return 'http://127.0.0.1:8000' + self.image_resized.url
        else:
            if self.image:
                self.image_resized = self.resize_image(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.image_resized.url
            else:
                return ''
            
    def resize_image(self, image, size=(800, 600)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
    
    def get_local_path(self):
        if self.audio_file:
            file_name = os.path.basename(self.audio_file.name)
            local_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)
            return local_path
        return None
