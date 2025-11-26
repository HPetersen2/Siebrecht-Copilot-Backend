from rest_framework import serializers
from basicdata.models import CustomerGroup, VehicleModel, Brand, VehicleType, PaydType

class CustomerGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = ['name']  

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class VehicleModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['name']

class VehicleTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['name']

class PaydTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaydType
        fields = ['name']