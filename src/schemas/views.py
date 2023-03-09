from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from schemas.forms import DataForm, DataFormSet, SchemaForm
from schemas.models import Schema


def form_set(request):
    form_schema = SchemaForm()
    form_set = DataFormSet()
    if request.method == "POST":
        form_set = DataFormSet(request.POST)
        form_schema = SchemaForm(request.POST)
        if form_schema.is_valid() and form_set.is_valid():
            schema = form_schema.save(commit=False)
            user = get_user_model().objects.get(pk=1)
            schema.user = user
            schema.save()
            for form in sorted(form_set, key=lambda form: form.cleaned_data.get('order')):
                if form.is_valid():
                    try:
                        instance = form.save(commit=False)
                        instance.schema = schema
                        instance.save()
                    except Exception as e:
                        print(f'Error: {e}')

            return redirect('schemas')

    context = {
        "formset": form_set,
        "schema_form": form_schema,
    }
    return render(request, "schemas/build_schema.html", context)


class GetSchemas(LoginRequiredMixin, ListView):
    model = Schema
    template_name = "schemas/schemas.html"
    context_object_name = "schemas"
    extra_context = {'title': 'Schemas'}
    raise_exception = True

    def get_queryset(self):
        schemas = Schema.objects.filter(user=self.request.user)
        return schemas


class DeleteSchema(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('schemas')
    raise_exception = True

