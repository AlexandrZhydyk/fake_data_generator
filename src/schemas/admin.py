from django.contrib import admin

from schemas.models import Schema, DataType

admin.site.register(Schema)
admin.site.register(DataType)

