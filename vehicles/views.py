from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions]