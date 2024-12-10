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
    
# from django.views import View
# from django.shortcuts import render
# from os import path

# from review.models import BankNiftyReview


# class Dashboard(View):
#     def get(self,request):
#         trades_summary=BankNiftyReview.objects.values().order_by('-inventory_on')
#         context={
#             'trades_summary':trades_summary
#         }
#         return render(request,path.join('core','dashboard.html'),context)



# def contact(request):

#     return render(request,path.join('core','contact.html'))

# def about(request):

#     return render(request,path.join('core','about.html'))

# def custom_404_view(request, exception):
#     print('404.html exel')
#     return render(request,path.join('core','404.html'), status=404)