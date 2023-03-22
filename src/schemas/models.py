from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Schema(models.Model):
    SEPARATORS = [
        (",", "Comma ( , )"),
        (";", "Semicolon ( ; )"),
        ("|", "Pipe ( | )"),
    ]

    name = models.CharField(max_length=60, null=True, blank=False)
    column_separator = models.CharField(max_length=1, choices=SEPARATORS, default=",")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Modified"
    )
    user = models.ForeignKey(
        get_user_model(), related_name="schemas", on_delete=models.CASCADE, null=True
    )


class DataType(models.Model):
    DATA_TYPES = [
        ("FN", "Fullname"),
        ("EM", "Email"),
        ("BR", "Birthdate"),
        ("DM", "Domain"),
        ("AD", "Address"),
        ("PN", "Phone number"),
        ("AG", "Age"),
        ("TX", "Text"),
    ]

    column_name = models.CharField(
        max_length=60, null=False, blank=True, verbose_name="Column name"
    )
    data_type = models.CharField(max_length=2, choices=DATA_TYPES, default="FN")
    ORDER = models.IntegerField(
        blank=True, validators=[MinValueValidator(limit_value=0)], default=0
    )
    schema = models.ForeignKey(
        Schema, related_name="data_type", on_delete=models.CASCADE, null=False
    )
    range_from = models.IntegerField(null=True, blank=True, verbose_name="From")
    range_to = models.IntegerField(null=True, blank=True, verbose_name="To")
