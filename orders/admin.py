from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'owner',
        'order_status',
        'created_at'
    ]
    search_fields = [
        'owner',
        'id'
    ]