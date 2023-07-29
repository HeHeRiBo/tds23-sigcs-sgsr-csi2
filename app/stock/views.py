from rest_framework import generics
from .models import Movimiento, Consumo
from .serializers import MovimientoSerializer, ConsumoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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


class ConsumoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer


class ConsumoMedicamentoView(generics.GenericAPIView):
    def get():
        pass


class DisponibilidadMedicamentoView(APIView):
    def get(self, request):
        data = {5: {"medicamento": 5, "cantidad": 500, "stocks": [{"institucion": 1, "cantidad": 500}]}}
        return Response(data)


class DisponibilidadMedicamentoDetailView(APIView):
    def get(self, request, medicamento_id):
        data = {}  # Si no se encuentra disponibilidad para el medicamento_id, devolver un diccionario vacío
        return Response(data)


class QuiebreStockView(APIView):
    def get(self, request):
        data = [{"institucion": 1, "medicamento": 5, "stock": 500, "quiebre": 500}]
        return Response(data)


class AlertaCaducidadLoteView(APIView):
    def get(self, request):
        data = [
            {
                "id": 16,
                "codigo": "SA_NAHRD_5j2mDrL9x0xKCl_20230721_20330721",
                "medicamento": 23,
                "cantidad": 450000,
                "fecha_vencimiento": "2022-07-21",
            },
            {
                "id": 17,
                "codigo": "SE_ASBRD_8N9uLf3P8qfNCl_20230730_20330730",
                "medicamento": 34,
                "cantidad": 775000,
                "fecha_vencimiento": "2022-07-30",
            },
            {
                "id": 18,
                "codigo": "TR_ABDRG_5p3WLiH4m7eFCl_20230726_20330726",
                "medicamento": 2,
                "cantidad": 575000,
                "fecha_vencimiento": "2022-07-26",
            },
        ]
        return Response(data)
