from rest_framework import serializers
from ..models import Product, Store, Warehouse, Catalog, Category


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
