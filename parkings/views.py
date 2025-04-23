from rest_framework import viewsets
from parkings.models import ParkingSpot, ParkingRecord
from parkings.serializers import ParkingSpotSerializer, ParkingRecordSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
