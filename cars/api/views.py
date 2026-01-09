from rest_framework import generics
from cars.models import Car
from cars.api.serializers import CarSerializer, CarNameSerializer
from .permissions import IsAuthenticatedWithCookie

class CarsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedWithCookie]

class CarsListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedWithCookie]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CarNameListView(generics.ListAPIView):
    queryset = Car.objects.all().only('id', 'customer_name')
    serializer_class = CarNameSerializer
    permission_classes = [IsAuthenticatedWithCookie]