from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Product, Writer, Publisher, Order, OrderItem, Blog, Contact
from .serializers import CategorySerializer, ProductSerializer, WriterSerializer, PublisherSerializer, OrderSerializer, BlogSerializer, ContactSerializer
from django.conf import settings  # Import settings here
from django.core.mail import send_mail  # Import send_mail here


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        order = Order.objects.create(
            name=data['name'],
            email=data.get('email', ''),
            phone_number=data['phone_number'],
            alt_phone_number=data.get('alt_phone_number', ''),
            country=data['country'],
            district=data['district'],
            area=data['area'],
            address_details=data['address_details'],
            total=data['total'],
            shipping_cost=data['shipping_cost'],
            grand_total=data['grand_total'],
            payment_method=data['payment_method']
        )

        products = data.get('products', [])
        for item in products:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)
            
            # Ensure the product exists
            try:
                product = Product.objects.get(id=product_id)
                price = product.price * quantity
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            except Product.DoesNotExist:
                return Response({"error": f"Product with id {product_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # Save the new Contact instance
        contact = serializer.save()

        # Prepare email details
        subject = 'New Contact Form Submission'
        message = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Phone: {contact.phone_number}\n"
            f"Message: {contact.message}"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [contact.email]  # Email address from the contact form
        
        # Send email
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Return the response
        return Response(serializer.data, status=status.HTTP_201_CREATED)