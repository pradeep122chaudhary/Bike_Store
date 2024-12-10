from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.
from django.shortcuts import render
from .models import DeliveryOrder
import json

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
    
class AddNewLead(View):
    template='new_lead.html'
    def get(self, request):
       
        return render(request, self.template)
    def post(self, request):
        
        customer = request.POST.get('customer')
     


        
        context={
            'title': 'Submitted!',
            'status':'error',
            'message':'data has been submitted.'
        }
        return JsonResponse(context)
    


    
class LeadsList(View):
    template='leads_list.html'
    def get(self, request):
        print('hello mohan')
        return render(request, self.template)
    def post(self, request):
        return render(request, self.template)
    

