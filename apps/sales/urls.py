from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"customers", views.CustomerViewSet, basename="customer")
router.register(r"sellers", views.SellerViewSet, basename="seller")
router.register(r"sales", views.SaleViewSet, basename="sale")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
