# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from discounts.models import Discount
from .serializers import DiscountSerializer


class DiscountView(APIView):

    def get(self, request, format=None):
        customer_group_name = request.GET.get('customer_group_name')
        vehicle_model_name = request.GET.get('vehicle_model_name')

        if not customer_group_name or not vehicle_model_name:
            return Response({"count": 0, "discounts": []})

        today = timezone.now().date()

        discounts = (
            Discount.objects.filter(
                customer_group__name__iexact=customer_group_name,
                model__name__iexact=vehicle_model_name,
                valid_from__lte=today,
                valid_to__gte=today,
            )
            .distinct()
        )

        serialized = DiscountSerializer(discounts, many=True).data

        filtered_discounts = []
        for d in serialized:
            if d["discount_type"] == "euro":
                filtered_discounts.append({
                    "discount_type": d["discount_type"],
                    "discount_name": d["discount_name"],
                    "discount_euro": d["discount_euro"],
                    "discount_euro_intern": d["discount_euro_intern"],
                })
            elif d["discount_type"] == "percent":
                filtered_discounts.append({
                    "discount_type": d["discount_type"],
                    "discount_name": d["discount_name"],
                    "discount_percent": d["discount_percent"],
                    "discount_percent_intern": d["discount_percent_intern"],
                })

        return Response({
            "count": len(filtered_discounts),
            "discounts": filtered_discounts
        })
