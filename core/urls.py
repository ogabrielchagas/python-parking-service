from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parkings.urls')),
    path('api/v1/', include('vehicles.urls')),
]
