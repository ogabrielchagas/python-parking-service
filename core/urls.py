from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parkings.urls')),
    path('api/v1/', include('vehicles.urls')),

    path('', admin.site.urls),  #URL root deve sempre vir por ultimo
]
