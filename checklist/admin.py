from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ChecklistItemTemplate

@admin.register(ChecklistItemTemplate)
class ChecklistItemTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    filter_horizontal = ("customer_groups", "brands", "vehicle_types", "payd_types")