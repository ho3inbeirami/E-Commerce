from product_module.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['id','title','price','is_active','is_delete']
