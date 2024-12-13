
from django.urls import path
from .views import LoginView,LogoutView,PasswordResetView
urlpatterns = [
    path('', LoginView.as_view(), name='LoginView'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),


    
]
