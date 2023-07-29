from rest_framework import generics
from .models import Movimiento, Consumo
from .serializers import MovimientoSerializer, ConsumoSerializer


class MovimientoListCreateView(generics.ListCreateAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class MovimientoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class MovimientoLoteRetrieveView(generics.RetrieveAPIView):
    pass


class MovimientoMedicamentoView(generics.GenericAPIView):
    def get():
        pass


class ConsumoListCreateView(generics.ListCreateAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer


class ConsumoRetrieveDestroyVie(generics.RetrieveDestroyAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer


class ConsumoMedicamentoView(generics.GenericAPIView):
    def get():
        pass


# class DisponibilidadMedicamentoView(views.APIView):
#     pass
