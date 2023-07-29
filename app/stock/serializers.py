from rest_framework import serializers
from .models import Lote, Consumo, Stock, Movimiento


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ["id", "codigo", "medicamento", "cantidad", "fecha_vencimiento"]


class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ["id", "institucion", "medicamento", "cantidad", "fecha"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "institucion", "medicamento", "cantidad", "has_quiebre", "fecha_actualizacion"]


class MovimientoSerializer(serializers.ModelSerializer):
    # No se si esta bien hacerlo asi
    """
    lote = serializers.PrimaryKeyRelatedField(
        queryset=Lote.objects.all(),
        validators=[UniqueValidator(queryset=Movimiento.objects.all(), message='Ya existe movimiento con este lote.')]
    )
    """

    class Meta:
        model = Movimiento
        fields = ["id", "institucion", "lote", "fecha"]
