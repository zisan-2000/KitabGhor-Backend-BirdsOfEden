from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, WriterViewSet, PublisherViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'writers', WriterViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
