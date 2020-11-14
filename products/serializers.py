from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id', 'title', 'slug', 'sort_description', 'description', 'price', 'image', 'active', 'created_at', 'updated_at']
        fields = '__all__'