from django.urls import path

from schemas.views import form_set, DeleteSchema, GetSchemas, update_schema

urlpatterns = [
    path("", GetSchemas.as_view(), name="schemas"),
    path("build_schema/", form_set, name="build_schema"),
    path("update/<int:pk>/", update_schema, name="update_schema"),
    path("delete/<int:pk>/", DeleteSchema.as_view(), name="delete_schemas"),
]
