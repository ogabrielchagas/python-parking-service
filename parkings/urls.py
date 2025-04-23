from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parkings.views import ParkingSpotViewSet, ParkingRecordViewSet


router = DefaultRouter()
router.register('parkings/spots', ParkingSpotViewSet)
router.register('parkings/records', ParkingRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]