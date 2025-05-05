from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

# Home Page
class Home(TemplateView):
    template_name = 'accounts/home.html'  # Home template

# Redirect to home
def profile_redirect(request):
    return redirect('home')  # Redirect to home page

# Login Page
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'accounts/login.html')  # If not POST, show login page

# Signup Page
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    return render(request, 'accounts/signup.html')  # Show signup page

# Dashboard (Ensure template path is correct)
@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')  # Ensure this path exists

# Recommendations Page
def recommendations_view(request):
    return render(request, 'app/recommendations.html')  # Ensure this template exists

# Articles Page
def articles_view(request):
    return render(request, 'app/articles.html')  # Ensure this template exists

# Profile Page
@login_required
def profile_view(request):
    return render(request, 'app/profile.html')  # Profile page for logged-in users

# Home Page View
def home(request):
    return render(request, 'recommendation.html', {'user': request.user})  # Show home page with user info


def custom_logout(request):
    logout(request)  # This logs out the user
    return redirect('dashboard') 