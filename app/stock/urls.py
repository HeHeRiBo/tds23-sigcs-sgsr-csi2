from django.urls import path

from .views import (
    MovimientoListCreateView,
    MovimientoRetrieveDestroyView,
    MovimientoLoteRetrieveView,
    MovimientoMedicamentoView,
    MovimientoMedicamentoDetailView,
    ConsumoListCreateView,
    ConsumoRetrieveDestroyView,
    ConsumoMedicamentoView,
    DisponibilidadMedicamentoView,
    DisponibilidadMedicamentoDetailView,
    QuiebreStockView,
    AlertaCaducidadLoteView,
)

app_name = "stock"
urlpatterns = [
    path("movimientos", MovimientoListCreateView.as_view(), name="movimiento-lc"),
    path("movimientos/<int:pk>", MovimientoRetrieveDestroyView.as_view(), name="movimiento-rud"),
    path("movimientos/<int:pk>/lote", MovimientoLoteRetrieveView.as_view(), name="movimiento-lote-lc"),
    path("movimientos-medicamento", MovimientoMedicamentoView.as_view(), name="movimiento-medicamento-l"),
    path("movimientos-medicamento/<int:medicamento>", MovimientoMedicamentoDetailView.as_view(), name="movimiento-medicamento-d"),
    path("consumos", ConsumoListCreateView.as_view(), name="consumo-c"),
    path("consumos/<int:pk>", ConsumoRetrieveDestroyView.as_view(), name="consumo-rud"),
    path("consumos-medicamento", ConsumoMedicamentoView.as_view(), name="consumo-medicamento-l"),
    path("consumos-medicamento/<int:medicamento>", ConsumoMedicamentoView.as_view(), name="consumo-medicamento-d"),
    path("disponibilidad-medicamento", DisponibilidadMedicamentoView.as_view(), name="disponibilidad-medicamento-l"),
    path(
        "disponibilidad-medicamento/<int:medicamento_id>",
        DisponibilidadMedicamentoDetailView.as_view(),
        name="disponibilidad-medicamento-d",
    ),
    path("quiebre-stock", QuiebreStockView.as_view(), name="quiebre-stock"),
    path("alerta-caducidad-lote", AlertaCaducidadLoteView.as_view(), name="alerta-caducidad-lote"),
]
