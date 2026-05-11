from rest_framework import serializers
from outflows.models import Outflow
from products.serializers import ProductSerializer


class OutflowSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Outflow
        fields = ['id', 'quantity', 'description', 'created_at', 'updated_at', 'product']
