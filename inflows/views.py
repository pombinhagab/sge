from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from rest_framework import generics

from app.utils.export import export_to_excel
from . import forms, models, serializers


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflows'
    permission_required = 'inflows.view_inflow'


def export_inflows_xlsx(request):
    inflows = models.Inflow.objects.select_related('supplier', 'product').all()

    headers = ['ID', 'Fornecedor', 'Produto', 'Quantidade', 'Criado em']

    def get_row(inflow):
        return [
            inflow.id,
            inflow.supplier.name if inflow.supplier else '',
            inflow.product.title if inflow.product else '',
            inflow.quantity,
            inflow.created_at.strftime('%d/%m/%Y %H:%M')
        ]

    return export_to_excel(inflows, headers, get_row, "inflows.xlsx")


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer


class InflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
