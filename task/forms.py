from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class InputIndexForm(forms.Form):
    """
    Форма отправки индекса
    """
    index = forms.IntegerField(validators=[
        MaxValueValidator(99),
        MinValueValidator(0)
    ], required=True, label="Input index")
    flag = forms.BooleanField(required=False, label="обновить список ?:")


class InputABCForm(forms.Form):
    """
    Форма отправки коофициентов квадратного уравнения
    """
    a = forms.FloatField(required=True, label="a:")
    b = forms.FloatField(required=True, label="b:")
    c = forms.FloatField(required=True, label="c:")
