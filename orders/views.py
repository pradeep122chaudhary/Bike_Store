from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DeliveryOrder

def order_list(request):
    orders = DeliveryOrder.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})
