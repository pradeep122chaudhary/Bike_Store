from django.shortcuts import render
from django.views import View


# Create your views here.
from django.shortcuts import render
from .models import DeliveryOrder

def order_list(request):
    orders = DeliveryOrder.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

class Dashboard(View):
    template='dashboard.html'
    def get(self, request):
        print('hello mohan')
        return render(request, self.template)

  
    def post(self, request):
        return render(request, self.template)
    