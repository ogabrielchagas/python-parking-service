from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from parkings.models import ParkingSpot, ParkingRecord
from parkings.serializers import ParkingSpotSerializer, ParkingRecordSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions]
