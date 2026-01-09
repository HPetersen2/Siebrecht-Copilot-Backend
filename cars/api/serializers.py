from rest_framework import serializers
from cars.models import Car
from basicdata.models import Brand, CustomerGroup, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode

class CarSerializer(serializers.ModelSerializer):
    customerName = serializers.CharField(source='customer_name')
    selectedBrand = serializers.CharField(write_only=True)
    selectedModel = serializers.CharField(write_only=True)
    selectedPayd = serializers.CharField(write_only=True)
    selectedVehicleType = serializers.CharField(write_only=True)
    selectedSellerChannel = serializers.CharField(write_only=True)
    selectedGroup = serializers.CharField(write_only=True, required=False)
    selectedPromotionCode = serializers.PrimaryKeyRelatedField(
        source='promotion_code', 
        queryset=PromotionCode.objects.all(), 
        allow_null=True,   # Erlaubt den Wert null/None
        required=False     # Erlaubt, dass der Key im JSON komplett fehlt
    )
    
    checklistState = serializers.JSONField(source='checklist_state', required=False)
    customPublicValues = serializers.JSONField(source='custom_public_values', required=False)
    
    taxID = serializers.CharField(source='tax_id', allow_null=True, required=False)
    
    brandName = serializers.CharField(source='brand.name', read_only=True)
    modelName = serializers.CharField(source='model.name', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'customerName', 'selectedBrand', 'selectedModel', 'selectedPayd', 
            'selectedVehicleType', 'selectedSellerChannel', 'selectedGroup',
            'selectedPromotionCode', 'taxID', 'upe', 'customPublicValues', 'checklistState',
            'creator', 'created_at', 'updated_at', 'brandName', 'modelName'
        ]
        read_only_fields = ('creator', 'created_at', 'updated_at', 'id')

    def _handle_foreign_keys(self, validated_data):
        """Hilfsmethode, um Strings in Model-Instanzen aufzulösen"""
        brand_name = validated_data.pop('selectedBrand', None)
        model_name = validated_data.pop('selectedModel', None)
        payd_name = validated_data.pop('selectedPayd', None)
        v_type_name = validated_data.pop('selectedVehicleType', None)
        channel_name = validated_data.pop('selectedSellerChannel', None)
        
        if brand_name:
            validated_data['brand'] = Brand.objects.get(name=brand_name)
        if model_name:
            validated_data['model'] = VehicleModel.objects.get(name=model_name)
        if payd_name:
            validated_data['payd_type'] = PaydType.objects.get(name=payd_name)
        if v_type_name:
            validated_data['vehicle_type'] = VehicleType.objects.get(name=v_type_name)
        if channel_name:
            validated_data['seller_channel'] = SellerChannel.objects.get(name=channel_name)
            
        if 'selectedGroup' not in validated_data:
            validated_data['customer_group'] = CustomerGroup.objects.first()

        return validated_data

    def create(self, validated_data):
        validated_data = self._handle_foreign_keys(validated_data)
        
        if 'creator' not in validated_data:
            validated_data['creator'] = self.context['request'].user
            
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self._handle_foreign_keys(validated_data)
        return super().update(instance, validated_data)
    

class CarNameSerializer(serializers.ModelSerializer):
    customerName = serializers.CharField(source='customer_name')

    class Meta:
        model = Car
        fields = ['id', 'customerName']