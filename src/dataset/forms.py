from django import forms

from dataset.models import DataSet


class DataSetForm(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = [
            "schema",
            "csv_data",
        ]