from django.db import models
from django.contrib.auth import get_user_model
from basicdata.models import Brand, CustomerGroup, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode

User = get_user_model()

class Car(models.Model):

    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    customer_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.PROTECT)
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT)
    payd_type = models.ForeignKey(PaydType, on_delete=models.PROTECT)
    promotion_code = models.ForeignKey(PromotionCode, on_delete=models.SET_NULL, null=True, blank=True)
    seller_channel = models.ForeignKey(SellerChannel, on_delete=models.PROTECT)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    tax_id = models.CharField(max_length=50, null=True, blank=True)
    upe = models.DecimalField(max_digits=10, decimal_places=2)
    custom_public_values = models.JSONField(default=dict)
    checklist_state = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Vorgang"
        verbose_name_plural = "Vorgänge"

    def __str__(self):
        return f"{self.customer_name} - {self.brand} {self.model}"
