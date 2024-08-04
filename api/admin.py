from django.contrib import admin

# Register your models here.
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'total', 'grand_total', 'payment_method')
    search_fields = ('name', 'email', 'phone_number')