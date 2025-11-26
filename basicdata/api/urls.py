from django.urls import path
from .views import CustomerGroupView, BrandsView, VehicleModelView, VehiclesTypeView, PaydTypeView

urlpatterns = [
    path('customer-groups/', CustomerGroupView.as_view(), name='customer-groups'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('vehicle-models/', VehicleModelView.as_view(), name='vehicle-models'),
    path('types/', VehiclesTypeView.as_view(), name='types'),
    path('payd-types/', PaydTypeView.as_view(), name='payd-types'),
]