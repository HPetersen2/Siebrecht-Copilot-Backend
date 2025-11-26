from django.db import models

class ChecklistItemTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    customer_groups = models.ManyToManyField('basicdata.CustomerGroup', blank=True)
    brands = models.ManyToManyField('basicdata.Brand', blank=True)
    vehicle_types = models.ManyToManyField('basicdata.VehicleType', blank=True)
    payd_types = models.ManyToManyField('basicdata.PaydType', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Checklisteninhalt"
        verbose_name_plural = "Checklisteninhalte"

    def __str__(self):
        return self.name
