import requests

from django.http import Http404, FileResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Genre, Product
from .serializers import ProductSerializer, GenreSerializer


class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class GenreProductsListView(APIView):
    def get(self, request, genre_slug, format=None):
        genre = get_object_or_404(Genre, slug=genre_slug)
        products = Product.objects.filter(genre=genre)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def download_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    file_path = product.get_local_path()
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = f'attachment; filename="{product.name}.mp3"'
    return response

