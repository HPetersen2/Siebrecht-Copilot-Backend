from django.urls import path
from .views import CarsCreateView

urlpatterns = [
    path('cars/', CarsCreateView.as_view(), name='create-cars'),
]