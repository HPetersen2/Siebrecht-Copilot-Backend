from django.db import models
from basicdata.models import VehicleModel, CustomerGroup
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Discount(models.Model):

    DISCOUNT_TYPE_CHOICES = [
        ('euro', 'Euro'),
        ('percent', 'Prozent'),
    ]

    discount_type = models.CharField(
        max_length=10,
        choices=DISCOUNT_TYPE_CHOICES,
        default='euro',
        verbose_name="Nachlasstyp"
    )

    discount_euro = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Nachlass in Euro",
        help_text="Hier wird die Marge für den Verkäufer eingetragen"
    )

    discount_euro_intern = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Nachlass in Euro intern",
        help_text="Hier wird unsere Marge eingetragen"
    )

    discount_percent = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
        verbose_name="Nachlass in Prozent",
        help_text="Prozentualer Rabatt für den Kunden"
    )

    discount_percent_intern = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
        verbose_name="Nachlass in Prozent intern",
        help_text="Interne Prozentmarge"
    )

    discount_name = models.CharField(
        max_length=100,
        verbose_name="Nachlassbezeichnung"
    )

    description = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Beschreibung",
        help_text="(optional)"
    )

    customer_group = models.ManyToManyField(
        CustomerGroup,
        verbose_name="Gültige Kundengruppen",
        help_text="..."
    )

    model = models.ManyToManyField(
        VehicleModel,
        verbose_name="Gültige Fahrzeugmodelle",
        help_text="..."
    )

    valid_from = models.DateField(
        verbose_name="Gültig ab",
        help_text="Ab diesem Datum wird der Nachlass im Siebrecht Copilot sichtbar"
    )

    valid_to = models.DateField(
        null=True,
        blank=True,
        verbose_name="Gültig bis",
        help_text="Nach Ablauf dieses Datums ist der Nachlass im Copilot nicht mehr sichtbar"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Nachlass"
        verbose_name_plural = "Nachlässe"

    def __str__(self):
        valid_from_str = self.valid_from.strftime("%d.%m.%Y")
        valid_to_str = self.valid_to.strftime("%d.%m.%Y") if self.valid_to else "offen"

        if self.discount_type == "euro" and self.discount_euro is not None:
            rabatt = f"{self.discount_euro} €"
        elif self.discount_type == "percent" and self.discount_percent is not None:
            rabatt = f"{self.discount_percent}%"
        else:
            rabatt = "keiner"

        return f"{self.discount_name} | Gültig von {valid_from_str} bis {valid_to_str} | Nachlass: {rabatt}"
