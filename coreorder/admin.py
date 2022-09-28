from django.contrib import admin
from .models import OrderType
# Register your models here.

class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ['student','service_type', 'academic_level', 
    'paper_type', 'subject_area', 'pages', 'deadline']
    list_filter = ['deadline', 'student', 'service_type', 'paper_type']
    search_fields = ['student', 'service_type']



admin.site.register(OrderType, OrderTypeAdmin)

