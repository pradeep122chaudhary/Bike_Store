from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import DeliveryOrder,BikeModel,StatusModel
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin

def order_list(request):
    orders = DeliveryOrder.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

class Dashboard(LoginRequiredMixin,View):
    template = 'dashboard.html'

    def get(self, request):

        return render(request, self.template)

    def post(self, request):

        return render(request, self.template)
    
    
class AddNewLead(View):
    template_name = 'new_lead.html'  

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
    



@login_required
def export_leads_to_excel(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        ids = data.get('ids', [])
        leads = DeliveryOrder.objects.filter(id__in=ids)
        if not leads.exists():
            return JsonResponse({'error': 'No data found to export'}, status=400)

        # Prepare data for export
        data = []
        for lead in leads:
            delivery_date = lead.delivery_date
            delivery_date_str = delivery_date.strftime('%d-%m-%y') if delivery_date else ''

            data.append({
                'ID': lead.id,
                'Customer Name': lead.customer_name,
                'Gender': lead.gender,
                'Mobile': lead.mobile,
                'Address': lead.full_address,
                'Delivery Date': delivery_date_str,
                'Bike Model': lead.bike_model,
                'Status': lead.status,
            })

        # Create DataFrame
        df = pd.DataFrame(data)
        # Export to Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="leads.xlsx"'
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Leads')

        return response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    

