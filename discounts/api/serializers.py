from rest_framework import serializers
from discounts.models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            "discount_type",
            "discount_euro",
            "discount_euro_intern",
            "discount_percent",
            "discount_percent_intern",
            "discount_name",
        ]