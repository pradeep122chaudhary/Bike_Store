from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BikeModel, DeliveryOrder, StatusModel, DeliveryOrderHistory

admin.site.register(BikeModel)


class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'mobile', 'gender', 'full_address', 'bike_model', 'created_by', 'created_at', 'delivery_date', 'status')
    search_fields = ('customer_name', 'mobile')
    list_filter = ('gender', 'status', 'created_at')

admin.site.register(DeliveryOrder, DeliveryOrderAdmin)

admin.site.register(StatusModel)
admin.site.register(DeliveryOrderHistory)
