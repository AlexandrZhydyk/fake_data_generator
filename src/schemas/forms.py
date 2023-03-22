from django import forms
from django.forms import (
    formset_factory,
    inlineformset_factory,
    BaseFormSet,
    BaseInlineFormSet,
)

from schemas.models import DataType, Schema


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


class BaseDataTypeFormSet(BaseFormSet):
    def get_ordering_widget(self):
        return forms.NumberInput(
            attrs={
                "class": "form-control",
                "value": 0,
                "required": "true",
                "min": 0,
            },
        )

    def get_deletion_widget(self):
        return forms.CheckboxInput(
            attrs={
                "class": "btn-check",
                "value": False,
                "min": 0,
                "autocomplete": "off",
            }
        )


class DataForm(forms.ModelForm):
    class Meta:
        model = DataType
        fields = ["column_name", "ORDER", "data_type", "range_from", "range_to"]
        widgets = {
            "column_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Column name",
                    "required": "true",
                }
            ),
            "data_type": forms.Select(attrs={"class": "form-select"}),
            "range_from": forms.TextInput(
                attrs={"class": "form-control", "hidden": "true"}
            ),
            "range_to": forms.TextInput(
                attrs={"class": "form-control", "hidden": "true"}
            ),
        }


DataFormSet = formset_factory(
    DataForm, formset=BaseDataTypeFormSet, can_order=True, can_delete=True
)


class CustomInlineFormSet(BaseInlineFormSet):
    def get_ordering_widget(self):
        return forms.NumberInput(
            attrs={
                "class": "form-control",
                "value": 0,
                "required": "true",
                "min": 0,
            },
        )

    def get_deletion_widget(self):
        return forms.CheckboxInput(
            attrs={
                "class": "btn-check",
                "value": False,
                "min": 0,
                "autocomplete": "off",
            }
        )


DataTypeFormSet = inlineformset_factory(
    Schema,
    DataType,
    extra=0,
    can_order=True,
    can_delete=True,
    formset=CustomInlineFormSet,
    fields=["ORDER", "column_name", "data_type", "range_from", "range_to"],
    labels={
        "ORDER": "Order",
    },
    widgets={
        "column_name": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Column name",
                "required": "true",
            }
        ),
        "data_type": forms.Select(attrs={"class": "form-select"}),
        "range_from": forms.TextInput(
            attrs={"class": "form-control", "hidden": "true"}
        ),
        "range_to": forms.TextInput(attrs={"class": "form-control", "hidden": "true"}),
    },
)
