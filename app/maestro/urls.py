from django.urls import path

from .views import (
    MedicamentoListCreateView,
    MedicamentoRetrieveDestroyView,
    EquipamientoListCreateView,
    EquipamientoRetrieveDestroyView,
    InstitucionListCreateView,
    InstitucionRetrieveDestroyView,
)

app_name = "maestro"
urlpatterns = [
    path("medicamentos", MedicamentoListCreateView.as_view(), name="medicamento-lc"),
    path("medicamentos/<int:pk>", MedicamentoRetrieveDestroyView.as_view(), name="medicamento-rud"),
    path("equipamientos", EquipamientoListCreateView.as_view(), name="equipamiento-lc"),
    path("equipamientos/<int:pk>", EquipamientoRetrieveDestroyView.as_view(), name="equipamiento-rud"),
    path("instituciones", InstitucionListCreateView.as_view(), name="institucion-lc"),
    path("instituciones/<int:pk>", InstitucionRetrieveDestroyView.as_view(), name="institucion-rud"),
]
