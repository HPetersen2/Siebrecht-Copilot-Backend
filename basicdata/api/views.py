from rest_framework import generics
from basicdata.models import CustomerGroup, Brand, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode
from .serializers import CustomerGroupListSerializer, BrandListSerializer, VehicleModelListSerializer, VehicleTypeListSerializer, PaydTypeListSerializer, SellerChannelListSerializer, PromotionCodeListSerializer

class CustomerGroupView(generics.ListAPIView):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupListSerializer

class BrandsView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class VehicleModelView(generics.ListAPIView):
    serializer_class = VehicleModelListSerializer

    def get_queryset(self):
        queryset = VehicleModel.objects.all()
        brand_name = self.request.query_params.get('brand')
        if brand_name:
            queryset = queryset.filter(brand__name=brand_name)
        return queryset

class VehiclesTypeView(generics.ListAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeListSerializer

class PaydTypeView(generics.ListAPIView):
    queryset = PaydType.objects.all()
    serializer_class = PaydTypeListSerializer

class SellerChannelView(generics.ListAPIView):
    queryset = SellerChannel.objects.all()
    serializer_class = SellerChannelListSerializer

class PromotionCodeView(generics.ListAPIView):
    queryset = PromotionCode.objects.all()
    serializer_class = PromotionCodeListSerializer