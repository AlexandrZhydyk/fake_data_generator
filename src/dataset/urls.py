from django.urls import path

from dataset.views import GetDataSets, data_generate

urlpatterns = [
    path('<int:schema_id>/', GetDataSets.as_view(), name='get_data_sets'),
    path('create_data/', data_generate, name='data_generate'),
]
