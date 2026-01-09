from django.urls import path
from .views import CarsDetailView, CarsListCreateView, CarNameListView

urlpatterns = [
    path('cars/', CarsListCreateView.as_view(), name='list-create-cars'),
    path('cars/<int:pk>/', CarsDetailView.as_view(), name='detail-cars'),
    path('cars/names/', CarNameListView.as_view(), name='car-names'),
]