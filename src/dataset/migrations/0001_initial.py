# Generated by Django 4.1.7 on 2023-03-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("schemas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created date"
                    ),
                ),
                (
                    "csv_data",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="%Y/%m/%d/",
                        verbose_name="CSV fake data",
                    ),
                ),
                (
                    "is_done",
                    models.BooleanField(
                        default=False, help_text="Defines if the report is done."
                    ),
                ),
                (
                    "schema",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data_set",
                        to="schemas.schema",
                    ),
                ),
            ],
        ),
    ]
