from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),  # Choose one as the main
    # path('', include('social_app.urls')),  # Comment this out or mount it under a different path
    
    ]


