from django.urls import path
from .views import DiscountView

urlpatterns = [
    path('discount/', DiscountView.as_view(), name='discount-view'),
]