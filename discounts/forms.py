from django import forms
from django.core.exceptions import ValidationError
from .models import Discount

class DiscountForm(forms.ModelForm):

    class Meta:
        model = Discount
        fields = "__all__"

    def clean(self):
        cleaned = super().clean()

        t = cleaned.get("discount_type")

        euro = cleaned.get("discount_euro")
        euro_i = cleaned.get("discount_euro_intern")

        percent = cleaned.get("discount_percent")
        percent_i = cleaned.get("discount_percent_intern")

        # 🛑 Sicherstellen, dass Felder des NICHT gewählten Typs LEER sind
        if t == "euro" and (percent or percent_i):
            raise ValidationError("Bei Euro-Rabatt dürfen keine Prozentwerte ausgefüllt werden.")

        if t == "percent" and (euro or euro_i):
            raise ValidationError("Bei Prozent-Rabatt dürfen keine Euro-Werte ausgefüllt werden.")

        # 🛑 Pflichtfelder abhängig vom Typ
        if t == "euro":
            if not euro or not euro_i:
                raise ValidationError("Bitte Euro-Rabatt UND internen Euro-Rabatt angeben.")

        if t == "percent":
            if not percent or not percent_i:
                raise ValidationError("Bitte Prozent-Rabatt UND internen Prozent-Rabatt angeben.")

        return cleaned
