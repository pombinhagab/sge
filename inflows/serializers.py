from rest_framework import serializers
from inflows.models import Inflow
from products.serializers import ProductSerializer
from suppliers.serializers import SupplierSerializer


class InflowSerializer(serializers.ModelSerializer):

    supplier = SupplierSerializer()
    product = ProductSerializer()

    class Meta:
        model = Inflow
        fields = ['id', 'quantity', 'description', 'created_at', 'updated_at', 'supplier', 'product']
