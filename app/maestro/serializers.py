from rest_framework import serializers


from .models import Institucion, Medicamento, Item, Equipamiento, Quiebre


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = [
            "id",
            "nombre",
            "tipo",
            "titularidad",
            "num_camas_uti",
            "num_camas_uci",
            "factor",
        ]


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = [
            "id",
            "nombre_comercial",
            "nombre_generico",
            "ingredientes",
            "concentracion",
            "forma_presentacion",
            "forma_farmaceutica",
            "via_administracion",
            "indicaciones_terapeuticas",
            "contraindicaciones",
            "efectos_secundarios",
            "instrucciones_dosificacion",
            "fabricante",
            "informacion_almacenamiento",
            "interacciones_medicamentosas",
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "nombre",
            "tipo",
        ]


class EquipamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamiento
        fields = [
            "id",
            "item",
            "marca",
            "modelo",
        ]


class QuiebreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiebre
        fields = [
            "id",
            "institucion",
            "medicamento",
            "cantidad",
        ]
