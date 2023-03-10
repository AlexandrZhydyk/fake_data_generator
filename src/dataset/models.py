from django.db import models

from schemas.models import Schema


class DataSet(models.Model):
    schema = models.ForeignKey(
        Schema, related_name="data_set", on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, editable=False, verbose_name="Created date"
    )
    csv_data = models.FileField(
        null=True, blank=True, upload_to="%Y/%m/%d/", verbose_name="CSV fake data"
    )
    is_done = models.BooleanField(
        default=False, help_text="Defines if the report is done."
    )
