from rest_framework import serializers
from cars.models import Car
from basicdata.models import Brand, CustomerGroup, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode

class CarSerializer(serializers.ModelSerializer):
    # -------- Frontend → Backend --------
    customerName = serializers.CharField(source='customer_name')

    selectedBrand = serializers.CharField(write_only=True)
    selectedModel = serializers.CharField(write_only=True)
    selectedPayd = serializers.CharField(write_only=True)
    selectedVehicleType = serializers.CharField(write_only=True)
    selectedSellerChannel = serializers.CharField(write_only=True)
    selectedGroup = serializers.CharField(write_only=True, required=False)
    selectedPromotionCode = serializers.CharField(
        write_only=True, required=False, allow_null=True
    )

    taxID = serializers.CharField(source='tax_id', allow_null=True, required=False)
    checklistState = serializers.JSONField(source='checklist_state', required=False)
    customPublicValues = serializers.JSONField(source='custom_public_values', required=False)

    # -------- Backend → Frontend (read only) --------
    brandName = serializers.CharField(source='brand.name', read_only=True)
    modelName = serializers.CharField(source='model.name', read_only=True)
    groupName = serializers.CharField(source='customer_group.name', read_only=True)
    vehicleTypeName = serializers.CharField(source='vehicle_type.name', read_only=True)
    paydName = serializers.CharField(source='payd_type.name', read_only=True)
    sellerChannelName = serializers.CharField(source='seller_channel.name', read_only=True)
    promotionCodeName = serializers.CharField(source='promotion_code.name', read_only=True)
    additionalCosts = serializers.JSONField(
        source='additional_costs',
        required=False
    )

    class Meta:
        model = Car
        fields = [
            'id',
            'offerNumber',
            'customerName',
            'upe',
            'taxID',

            # write-only
            'selectedBrand',
            'selectedModel',
            'selectedPayd',
            'selectedVehicleType',
            'selectedSellerChannel',
            'selectedGroup',
            'selectedPromotionCode',

            # read-only
            'brandName',
            'modelName',
            'groupName',
            'vehicleTypeName',
            'paydName',
            'sellerChannelName',
            'promotionCodeName',
            'additionalCosts',

            'customPublicValues',
            'checklistState',
            'creator',
            'created_at',
            'updated_at',
        ]

        read_only_fields = ('id', 'creator', 'created_at', 'updated_at')

    # ----------------- FK-Auflösung -----------------

    def _handle_foreign_keys(self, validated_data):
        brand = validated_data.pop('selectedBrand', None)
        model = validated_data.pop('selectedModel', None)
        payd = validated_data.pop('selectedPayd', None)
        v_type = validated_data.pop('selectedVehicleType', None)
        channel = validated_data.pop('selectedSellerChannel', None)
        group = validated_data.pop('selectedGroup', None)
        promo = validated_data.pop('selectedPromotionCode', None)

        if brand:
            validated_data['brand'] = Brand.objects.get(name=brand)
        if model:
            validated_data['model'] = VehicleModel.objects.get(name=model)
        if payd:
            validated_data['payd_type'] = PaydType.objects.get(name=payd)
        if v_type:
            validated_data['vehicle_type'] = VehicleType.objects.get(name=v_type)
        if channel:
            validated_data['seller_channel'] = SellerChannel.objects.get(name=channel)

        if group:
            validated_data['customer_group'] = CustomerGroup.objects.get(name=group)
        else:
            validated_data['customer_group'] = CustomerGroup.objects.first()

        if promo:
            validated_data['promotion_code'] = PromotionCode.objects.get(name=promo)
        else:
            validated_data['promotion_code'] = None

        return validated_data

    def create(self, validated_data):
        validated_data = self._handle_foreign_keys(validated_data)
        validated_data.setdefault('creator', self.context['request'].user)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self._handle_foreign_keys(validated_data)
        return super().update(instance, validated_data)

class CarNameSerializer(serializers.ModelSerializer):
    customerName = serializers.CharField(source='customer_name')

    class Meta:
        model = Car
        fields = ['id', 'customerName']