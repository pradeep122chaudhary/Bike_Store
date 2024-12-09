# myapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        return redirect('Dashboard')
        print(email, password)
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            print('hellow')
    #         messages.success(self.request, "Login successful!")
           
        return render(request, self.template_name)


    # def form_valid(self, form):
    #     username = 
       
    #     if user is not None:
    #          user = authenticate(self.request, username=username, password=password)
        
    #         login(self.request, user)
    #         messages.success(self.request, "Login successful!")
    #         return redirect('home')  # Redirect to home or dashboard
    #     else:
    #         messages.error(self.request, "Invalid username or password")
    #         return self.form_invalid(form)
