from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from dataset.models import DataSet
from dataset.utils.build_df import build_dataframe, create_data_set
from schemas.models import Schema, DataType
from dataset.utils.data_generator import FakeDataGenerator


def create_form_for_data_type(request):
    return render(request, "data_sets/data_set.html")


def data_generate(request, faker=FakeDataGenerator()):
    response_data = {}
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        schema_id = request.GET.get("schema_id")
        row_qty = int(request.GET.get("rows"))
        schema = Schema.objects.get(pk=schema_id)
        data_types = DataType.objects.filter(schema=schema)
        df = build_dataframe(data_types, row_qty, faker)
        data_set = create_data_set(schema, df)
        response_data["is_done"] = data_set.is_done
        response_data["csv_data"] = data_set.csv_data.url
        response_data["created_at"] = data_set.created_at
        return JsonResponse(response_data, status=200)
    else:
        return HttpResponseBadRequest("Invalid request")


class GetDataSets(LoginRequiredMixin, View):
    model = DataSet
    template_name = "data_sets/data_set.html"
    context_object_name = "data_sets"
    extra_context = {"title": "Data sets"}
    raise_exception = True

    def get(self, request, *args, **kwargs):
        schema_id = kwargs.get("schema_id")
        schema = Schema.objects.get(pk=schema_id)
        data_types = DataType.objects.filter(schema=schema)
        data_sets = DataSet.objects.filter(schema__user=self.request.user)
        return render(
            request,
            self.template_name,
            {"data_sets": data_sets, "data_types": data_types, "schema": schema},
        )
