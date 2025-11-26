from rest_framework import generics
from django.db.models import Q
from checklist.models import ChecklistItemTemplate
from .serializers import ChecklistItemTemplateSerializer
from basicdata.models import CustomerGroup, Brand, VehicleType, PaydType

class ChecklistItemTemplateListView(generics.ListAPIView):
    serializer_class = ChecklistItemTemplateSerializer

    def resolve_filter(self, model, param_value, name_field="name"):
        if not param_value:
            return None

        if str(param_value).isdigit():
            return model.objects.filter(id=param_value).first()

        filters = {name_field: param_value}
        return model.objects.filter(**filters).first()

    def get_queryset(self):
        customer_group = self.resolve_filter(CustomerGroup, self.request.query_params.get('customer_group'))
        brand = self.resolve_filter(Brand, self.request.query_params.get('brand'))
        vehicle_type = self.resolve_filter(VehicleType, self.request.query_params.get('vehicle_type'))
        payd_type = self.resolve_filter(PaydType, self.request.query_params.get('payd_type'))

        queryset = ChecklistItemTemplate.objects.filter(
            Q(customer_groups__isnull=True) | Q(customer_groups=customer_group),
            Q(brands__isnull=True) | Q(brands=brand),
            Q(vehicle_types__isnull=True) | Q(vehicle_types=vehicle_type),
            Q(payd_types__isnull=True) | Q(payd_types=payd_type),
        ).distinct()

        return queryset