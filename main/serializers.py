from rest_framework import serializers
from .models import Product, Get


class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Get
        field = ("name", "photo", "hope_price")


class PostProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        filed = ("name", "content", "price", "photo")
