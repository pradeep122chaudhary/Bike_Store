from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import Q


# Create your views here.
from django.shortcuts import render
from .models import DeliveryOrder,BikeModel,StatusModel
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
    template_name = 'new_lead.html'  # Matches your template file name

    def get(self, request):
        status = StatusModel.objects.all()
        bike_models = BikeModel.objects.all()
        return render(request, self.template_name, {'bike_models': bike_models,'status': status})

    def post(self, request):
        customer = request.POST.get('customer', '').strip()  
        mobile = request.POST.get('mobile', '')
        gender = request.POST.get('gender_id', '')
        full_address = request.POST.get('address_id', '').strip()  
        bike_model_id = request.POST.get('bike_model', '')
        created_by = request.user
        # Validate and save the data to the database.  In a real-world application, you'd also want to handle errors gracefully.
        try:
            bike_model = BikeModel.objects.get(id=bike_model_id)
            DeliveryOrder.objects.create(
                customer_name=customer,
                mobile=mobile,
                gender=gender,
                full_address=full_address,
                bike_model=bike_model,
                created_by=created_by,
                delivery_date=request.POST.get('delivery_date'),
                status_id=1
            )
            context = {
                'title': 'Success!',
                'status': 'success',
                'message': 'Data has been submitted successfully.'
            }
        except Exception as e:
            context = {
                'title': 'Error!',
                'status': 'error',
                'message': str(e)
            }
        return JsonResponse(context)

    
class LeadsList(View):
    template='leads_list.html'
    def get(self, request):
        search_query = request.GET.get('search', '')
        leads = DeliveryOrder.objects.all().order_by('-id')

        # If there is a search query, filter the leads based on the search criteria
        # if search_query:
        #     # Use Q objects for multiple OR conditions on different fields
        #     leads = leads.filter(
        #         Q(customer_name__icontains=search_query) |
        #         Q(mobile__icontains=search_query) |
        #         Q(full_address__icontains=search_query) |
        #         Q(delivery_date__icontains=search_query) |
        #         Q(bike_model__model__icontains=search_query) |  
        #         Q(status__name__icontains=search_query)  
        #     )

        return render(request, self.template, {'leads': leads})
    def post(self, request):
        return render(request, self.template)
    

