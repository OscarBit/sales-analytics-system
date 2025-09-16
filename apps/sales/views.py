from rest_framework import viewsets
from .models import Product, Customer, Seller, Sale
from .serializers import (
    ProductSerializer,
    CustomerSerializer,
    SellerSerializer,
    SaleSerializer,
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by("name")
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows customers to be viewed.
    """

    queryset = Customer.objects.all().order_by("name")
    serializer_class = CustomerSerializer


class SellerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows sellers to be viewed.
    """

    queryset = Seller.objects.all().order_by("name")
    serializer_class = SellerSerializer


class SaleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows sales to be viewed.
    This ViewSet is optimized for performance using `select_related`.
    """

    serializer_class = SaleSerializer

    def get_queryset(self):
        """
        Optimize the queryset by pre-fetching related objects in a single
        database query. This avoids the "N+1 query problem".
        """
        return Sale.objects.select_related("product", "customer", "seller").all()
