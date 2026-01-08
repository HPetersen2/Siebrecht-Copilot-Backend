from rest_framework import serializers
from cars.models import Car
from basicdata.models import Brand, CustomerGroup, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode

class CarSerializer(serializers.ModelSerializer):
    selectedBrand = serializers.CharField(write_only=True)
    selectedGroup = serializers.CharField(write_only=True)
    selectedModel = serializers.CharField(write_only=True)
    selectedPayd = serializers.CharField(write_only=True)
    selectedPromotionCode = serializers.CharField(write_only=True, required=False, allow_null=True)
    selectedSellerChannel = serializers.CharField(write_only=True)
    selectedVehicleType = serializers.CharField(write_only=True)
    customPublicValues = serializers.JSONField(source='custom_public_values')
    customerName = serializers.CharField(source='customer_name')
    taxID = serializers.CharField(source='tax_id', required=False, allow_null=True)

    class Meta:
        model = Car
        fields = ['selectedBrand', 'selectedGroup', 'selectedModel', 'selectedPayd', 'selectedPromotionCode', 'selectedSellerChannel', 'selectedVehicleType', 'customPublicValues', 'customerName', 'taxID', 'upe', 'creator', 'created_at', 'updated_at']
        read_only_fields = ('creator', 'created_at', 'updated_at')

    def create(self, validated_data):
        selected_brand = validated_data.pop('selectedBrand')
        selected_group = validated_data.pop('selectedGroup')
        selected_model = validated_data.pop('selectedModel')
        selected_payd = validated_data.pop('selectedPayd')
        selected_promotion_code = validated_data.pop('selectedPromotionCode')
        selected_seller_channel = validated_data.pop('selectedSellerChannel')
        selected_vehicle_type = validated_data.pop('selectedVehicleType')

        brand = Brand.objects.get(name=selected_brand)
        customer_group = CustomerGroup.objects.get(name=selected_group)
        model = VehicleModel.objects.get(name=selected_model, brand=brand)
        payd_type = PaydType.objects.get(name=selected_payd)
        seller_channel = SellerChannel.objects.get(name=selected_seller_channel)
        vehicle_type = VehicleType.objects.get(name=selected_vehicle_type)
        promotion_code = None
        if selected_promotion_code:
            promotion_code = PromotionCode.objects.get(name=selected_promotion_code)

        car = Car.objects.create(
            brand=brand,
            customer_group=customer_group,
            model=model,
            payd_type=payd_type,
            seller_channel=seller_channel,
            vehicle_type=vehicle_type,
            promotion_code=promotion_code,
            **validated_data
        )
        return car