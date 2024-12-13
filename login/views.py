from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Dashboard')
        
        next_url = request.GET.get('next', '')

        # Pass 'next' to the template context so that it can be used in the login form
        return render(request, self.template_name, {'next': next_url})
        # return render(request, self.template_name)
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Custom authentication using email
        try:
            user = User.objects.get(email=email)
            user = authenticate(self.request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Login successful!")
            # return redirect('Dashboard')  
            next_url = request.POST.get('next', request.GET.get('next', 'Dashboard'))
            return redirect(next_url)
        else:
            messages.error(self.request, "Invalid email or password.")
            return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        # Log the user out
        logout(request)
        
        # Optionally add a message (e.g., "Logged out successfully")
        messages.success(request, "You have been logged out successfully.")
        
        # Redirect to login page or home page
        return redirect('LoginView') 
    




class PasswordResetView(LoginRequiredMixin, View):
    # URL requires the user to be logged in
    login_url = 'LoginView'  

    def get(self, request, *args, **kwargs):
        """
        Display the password reset form to the user.
        """
        return render(request, 'password_reset.html')

    def post(self, request, *args, **kwargs):
        """
        Handle the password reset logic.
        """
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate if new passwords match
        if new_password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'The new passwords do not match.'}, status=400)

        # Authenticate the old password
        user = authenticate(username=request.user.username, password=old_password)
        if user is not None:
            # Set new password
            user.set_password(new_password)
            user.save()

            # Update session to prevent logout after password change
            update_session_auth_hash(request, user)

            return JsonResponse({'status': 'success', 'message': 'Your password has been reset successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Old password is incorrect.'}, status=400)

