import django_filters
from .models import Sale


class SaleFilter(django_filters.FilterSet):
    sale_date = django_filters.DateFromToRangeFilter()

    product_category = django_filters.CharFilter(
        field_name="product__category", lookup_expr="icontains"
    )
    customer_region = django_filters.CharFilter(
        field_name="customer__region", lookup_expr="iexact"
    )

    class Meta:
        model = Sale
        fields = ["sale_date", "product_category", "customer_region"]
