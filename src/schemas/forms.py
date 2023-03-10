from django import forms
from django.forms import formset_factory

from schemas.models import DataType, Schema


class DataForm(forms.ModelForm):
    class Meta:
        model = DataType
        fields = ["column_name", "data_type", "order", "range_from", "range_to"]
        widgets = {
            "column_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Column name",
                    "required": "true",
                }
            ),
            "data_type": forms.Select(attrs={"class": "form-select"}),
            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "value": 0,
                    "required": "true",
                    "min": 0,
                }
            ),
            "range_from": forms.TextInput(
                attrs={"class": "form-control", "hidden": "true"}
            ),
            "range_to": forms.TextInput(
                attrs={"class": "form-control", "hidden": "true"}
            ),
        }


DataFormSet = formset_factory(DataForm)


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = [
            "name",
            "column_separator",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Schema name"}
            ),
            "column_separator": forms.Select(attrs={"class": "form-select"}),
        }
