from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CustomerGroup, Brand, VehicleModel, VehicleType, PaydType, SellerChannel, PromotionCode

admin.site.register(CustomerGroup, ImportExportModelAdmin)
admin.site.register(Brand, ImportExportModelAdmin)
admin.site.register(VehicleModel, ImportExportModelAdmin)
admin.site.register(VehicleType, ImportExportModelAdmin)
admin.site.register(PaydType, ImportExportModelAdmin)
admin.site.register(SellerChannel, ImportExportModelAdmin)
admin.site.register(PromotionCode, ImportExportModelAdmin)