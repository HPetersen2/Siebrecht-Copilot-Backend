from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from .models import ChecklistItemTemplate

@admin.register(ChecklistItemTemplate)
class ChecklistItemTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    filter_horizontal = ("customer_groups", "brands", "vehicle_types", "payd_types")

    list_filter = (
        ('customer_groups', RelatedOnlyFieldListFilter),
        ('brands', RelatedOnlyFieldListFilter),
        ('vehicle_types', RelatedOnlyFieldListFilter),
        ('payd_types', RelatedOnlyFieldListFilter),
    )
