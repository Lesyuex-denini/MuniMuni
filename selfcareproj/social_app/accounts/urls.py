from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),            # Root path
    path('dashboard/', views.dashboard, name='dashboard'),  # <-- Add this line
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.Home.as_view(), name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
     path('articles/', views.articles_view, name='articles'),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),
   



]
