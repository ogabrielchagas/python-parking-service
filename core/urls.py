from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parkings.urls')),
    path('api/v1/', include('vehicles.urls')),

    path('', admin.site.urls),  #URL root deve sempre vir por ultimo
]
