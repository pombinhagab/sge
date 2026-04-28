from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outlows/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outlows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),

    path('outflows/export/', views.export_outflows_xlsx, name='export_outflows')
]
