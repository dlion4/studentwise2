from django.contrib import admin
from .models import OrderType, OrderItem


# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderTypeAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['student', 'service_type', 'academic_level',
                    'paper_type', 'subject_area', 'pages', 'words', 'prices', 'deadline']
    list_filter = ['deadline', 'student', 'service_type', 'paper_type']
    search_fields = ['student', 'service_type']


admin.site.register(OrderType, OrderTypeAdmin)
