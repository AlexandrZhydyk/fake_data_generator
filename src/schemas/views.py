from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView

from schemas.forms import DataFormSet, SchemaForm, DataTypeFormSet
from schemas.models import Schema


def create_schema(request):
    form_schema = SchemaForm()
    form_set = DataFormSet()
    if request.method == "POST":
        form_set = DataFormSet(request.POST)
        form_schema = SchemaForm(request.POST)
        if form_schema.is_valid() and form_set.is_valid():
            schema = form_schema.save(commit=False)
            user = get_user_model().objects.get(pk=request.user.pk)
            schema.user = user
            schema.save()
            for form in form_set.ordered_forms:
                try:
                    if form.is_valid():
                        instance = form.save(commit=False)
                        instance.schema = schema
                        instance.save()
                except Exception as e:
                    print(f"Error: {e}")

            return redirect("schemas")

    context = {
        "formset": form_set,
        "schema_form": form_schema,
    }
    return render(request, "schemas/build_schema.html", context)


class GetSchemas(LoginRequiredMixin, ListView):
    model = Schema
    template_name = "schemas/schemas.html"
    context_object_name = "schemas"
    extra_context = {"title": "Schemas"}
    raise_exception = True

    def get_queryset(self):
        schemas = Schema.objects.filter(user=self.request.user)
        return schemas


def update_schema(request, pk):
    schema = Schema.objects.get(pk=pk)
    form_schema = SchemaForm(instance=schema)
    formset = DataTypeFormSet(instance=schema)
    if request.method == "POST":
        form_schema = SchemaForm(request.POST)
        formset = DataTypeFormSet(request.POST, instance=schema)
        if formset.is_valid() and form_schema.is_valid():
            form_schema.save()
            instances = formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
            for instance in instances:
                instance.schema = schema
                instance.save()
            return redirect("schemas")

    context = {
        "schema": form_schema,
        "formset": formset,
    }
    return render(request, "schemas/update_schemas.html", context)


class DeleteSchema(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy("schemas")
    raise_exception = True
