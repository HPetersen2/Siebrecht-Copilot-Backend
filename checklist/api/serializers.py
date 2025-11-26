from rest_framework import serializers
from checklist.models import ChecklistItemTemplate

class ChecklistItemTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItemTemplate
        fields = ['name']