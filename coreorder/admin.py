from django.contrib import admin
from .models import OrderType, OrderItem


# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderTypeAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['student', 'task_type', 'academic_level',
                    'task_type', 'pages', 'words', 'prices', 'deadline']
    list_filter = ['deadline', 'student', 'task_type']
    search_fields = ['student', 'task_type']


admin.site.register(OrderType, OrderTypeAdmin)
