# from django.urls import path

# from .views import (
#     MovimientoListCreateView,
#     MovimientoRetrieveDestroyView,
#     MovimientoLoteRetrieveView,
#     MovimientoMedicamentoView,
#     ConsumoListCreateView,
#     ConsumoRetrieveDestroyVie,
# )

# app_name = "stock"
# urlpatterns = [
#     path("movimientos", MovimientoListCreateView.as_view(), name="movimiento-lc"),
#     path("movimientos/<int:pk>", MovimientoRetrieveDestroyView.as_view(), name="movimiento-rud"),
#     path("movimientos/<int:pk>/lote", MovimientoLoteRetrieveView.as_view(), name="movimiento-lote-lc"),
#     path("movimientos-medicamento", MovimientoMedicamentoView.as_view(), name="movimiento-medicamento-l"),
#     path("movimientos-medicamento/<int:medicamento>", MovimientoMedicamentoView.as_view(), name="movimiento-medicamento-d"),
#     path("consumos", ConsumoListCreateView.as_view(), name="consumo-c"),
#     path("consumos/<int:pk>", ConsumoRetrieveDestroyVie.as_view(), name="consumo-rud"),
# ]
