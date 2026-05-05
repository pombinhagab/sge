from rest_framework import serializers
from brands.serializers import BrandSerializer
from categories.serializers import CategorySerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at']
