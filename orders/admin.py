from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BikeModel, DeliveryOrder, StatusModel, DeliveryOrderHistory

admin.site.register(BikeModel)
admin.site.register(DeliveryOrder)
admin.site.register(StatusModel)
admin.site.register(DeliveryOrderHistory)
