from rest_framework import viewsets
from .models import Category, Product, Writer, Publisher
from .serializers import CategorySerializer, ProductSerializer, WriterSerializer, PublisherSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# existing views remain unchanged
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
