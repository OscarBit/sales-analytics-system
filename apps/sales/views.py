from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SaleFilter
from .models import Product, Customer, Seller, Sale
from .serializers import (
    ProductSerializer,
    CustomerSerializer,
    SellerSerializer,
    SaleSerializer,
)

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from django.db.models.functions import TruncMonth


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

    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleFilter

    def get_queryset(self):
        """
        Optimize the queryset by pre-fetching related objects in a single
        database query. This avoids the "N+1 query problem".
        """
        return Sale.objects.select_related("product", "customer", "seller").all()


class AnalyticsViewSet(ViewSet):
    """
    A ViewSet for delivering aggregated analytics data.
    This is a simple ViewSet, not a ModelViewSet, because we are not
    operating on a single model but providing custom aggregate queries.
    """

    def list(self, request):
        return Response({"detail": "This is the root for analytics endpoints."})

    @action(detail=False, methods=["get"])
    def monthly_revenue(self, request):
        """
        Calculates the total sales revenue for each month.
        """
        data = (
            Sale.objects.annotate(month=TruncMonth("sale_date"))
            .values("month")
            .annotate(total_revenue=Sum("sale_amount"))
            .order_by("month")
        )
        for item in data:
            if item["month"]:
                item["month"] = item["month"].strftime("%Y-%m-%d")
        return Response(data)

    @action(detail=False, methods=["get"])
    def category_revenue(self, request):
        """
        Calculates the total sales revenue for each product category.
        """
        queryset = Sale.objects.all()

        # --- Apply region filter ---
        region = request.query_params.get("region")
        if region:
            queryset = queryset.filter(customer__region=region)

        data = (
            queryset.values("product__category")
            .annotate(total_revenue=Sum("sale_amount"))
            .order_by("-total_revenue")
            # Rename the key to be consistent
            .values("product__category", "total_revenue")
        )
        return Response(
            [
                {
                    "category": item["product__category"],
                    "total_revenue": item["total_revenue"],
                }
                for item in data
            ]
        )

    @action(detail=False, methods=["get"])
    def top_sellers(self, request):
        """
        Identifies the top 10 sellers by total revenue.
        """
        data = (
            Seller.objects.annotate(total_revenue=Sum("sale__sale_amount"))
            .order_by("-total_revenue")[:10]
            .values("name", "total_revenue")
        )
        return Response(data)

    @action(detail=False, methods=["get"])
    def region_sales(self, request):
        """
        Calculates the total sales revenue for each customer region.
        """
        data = (
            Customer.objects.values("region")
            .annotate(total_revenue=Sum("sale__sale_amount"))
            .order_by("-total_revenue")
        )
        return Response(data)
