from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export.admin import ImportExportModelAdmin
from .models import Discount
from .forms import DiscountForm

@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
    form = DiscountForm
    list_display = ('discount_name', 'valid_period', 'discount_amount', 'model_list')
    list_filter = (
        'discount_type',
        'valid_from',
        'valid_to',
        ('model', RelatedOnlyFieldListFilter),
    )
    search_fields = ('discount_name', 'description')
    ordering = ('-valid_from',)

    def valid_period(self, obj):
        valid_from = obj.valid_from.strftime("%d.%m.%Y")
        valid_to = obj.valid_to.strftime("%d.%m.%Y") if obj.valid_to else "offen"
        return f"{valid_from} – {valid_to}"
    valid_period.short_description = "Gültig von/bis"

    def discount_amount(self, obj):
        if obj.discount_type == "euro" and obj.discount_euro is not None:
            return f"{obj.discount_euro} €"
        elif obj.discount_type == "percent" and obj.discount_percent is not None:
            return f"{obj.discount_percent}%"
        else:
            return "keiner"
    discount_amount.short_description = "Nachlasshöhe Kunde"

    def model_list(self, obj):
        return ", ".join([m.name for m in obj.model.all()])
    model_list.short_description = "Fahrzeugmodelle"

    class Media:
        js = ('admin/js/discount_toggle.js',)
