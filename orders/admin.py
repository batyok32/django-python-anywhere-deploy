from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields=['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email',
                    'address', 'city', 'phone_number',
                    'created', 'updated']

    list_filter = ['created', 'updated']
    inlines=[OrderItemInline]