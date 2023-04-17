from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repsesention = super().to_representation(instance)
        repsesention['products'] = [{'title': product.title, 'slug': product.slug} for product in instance.products.all()]
        return repsesention
    
