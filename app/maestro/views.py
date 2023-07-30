from rest_framework import generics
from .models import Institucion, Medicamento, Equipamiento
from .serializers import InstitucionSerializer, MedicamentoSerializer, EquipamientoSerializer


class InstitucionListCreateView(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class InstitucionRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


class MedicamentoListCreateView(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class MedicamentoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class EquipamientoListCreateView(generics.ListCreateAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer


class EquipamientoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer
