from django.db import models

class CustomerGroup(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kundengruppe"
        verbose_name_plural = "Kundengruppen"

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hersteller"
        verbose_name_plural = "Hersteller"

    def __str__(self):
        return self.name
    
class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Fahrzeugmodell"
        verbose_name_plural = "Fahrzeugmodelle"

    def __str__(self):
        return f"{self.brand} | {self.name}"

class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Fahrzeugtyp"
        verbose_name_plural = "Fahrzeugtypen"

    def __str__(self):
        return self.name
    
class PaydType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bezahlungsart"
        verbose_name_plural = "Bezahlungsarten"

    def __str__(self):
        return self.name