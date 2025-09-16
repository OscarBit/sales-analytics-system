from rest_framework import serializers
from .models import Customer, Seller, Product, Sale


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    """
    Main serializer for the Sale model.
    Uses nested serializers for related objects to provide rich, detailed output.
    These nested serializers are read-only, as we'll manage related objects
    separately.
    """

    product = ProductSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    seller = SellerSerializer(read_only=True)

    class Meta:
        model = Sale
        fields = [
            "sale_id",
            "sale_amount",
            "sale_date",
            "product",
            "customer",
            "seller",
            "created_at",
        ]
