from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, WriterViewSet, PublisherViewSet, OrderViewSet, BlogViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'writers', WriterViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'contacts', ContactViewSet)  # Add this line

urlpatterns = [
    path('', include(router.urls)),
]
