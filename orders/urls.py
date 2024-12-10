from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('home/', views.Dashboard.as_view(), name='Dashboard'),
    path('new/lead/', views.AddNewLead.as_view(), name='AddNewLead'),
    path('leads/view', views.LeadsList.as_view(), name='LeadsList'),

]
