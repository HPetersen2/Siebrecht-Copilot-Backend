from rest_framework import generics, status
from rest_framework.response import Response
from cars.models import Car
from cars.api.serializers import CarSerializer

class CarsCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)