import pytest
import json
from maestro.models import Institucion, Medicamento, Item, Equipamiento, Quiebre


@pytest.mark.django_db
def test_institucion_serializer():
    from maestro.serializers import InstitucionSerializer

    institucion = Institucion.objects.create(
        nombre="Hospital felix bulnes de prado y ochagavia",
        tipo=Institucion.Tipo.HOSPITAL,
        titularidad=Institucion.Titularidad.PUBLICO,
        num_camas_uti=10,
        num_camas_uci=5,
        factor=0.5,
    )
    data = {
        "id": institucion.id,
        "nombre": institucion.nombre,
        "tipo": institucion.tipo,
        "titularidad": institucion.titularidad,
        "num_camas_uti": institucion.num_camas_uti,
        "num_camas_uci": institucion.num_camas_uci,
        "factor": institucion.factor,
    }

    serialized_data = InstitucionSerializer(data=data)
    serialized_object = InstitucionSerializer(institucion)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_medicamento_serializer():
    from maestro.serializers import MedicamentoSerializer

    medicamento = Medicamento.objects.create(
        nombre_comercial="Panadol",
        nombre_generico="Paracetamol",
        ingredientes="Ácido Acetil Acetílico",
        concentracion="20 gr/kg",
        forma_presentacion=Medicamento.FormaPresentacion.FRASCO,
        forma_farmaceutica=Medicamento.FormaFarmaceutica.TABLETAS,
        via_administracion=Medicamento.Via.ORAL,
        indicaciones_terapeuticas="tome con abundante agua",
        contraindicaciones="no tomar estando embarazada",
        efectos_secundarios="dolor estomacal",
        instrucciones_dosificacion="1 tableta cada 6 horas",
        fabricante="SAVAL",
        informacion_almacenamiento="Guardar en un lugar fresco y oscuro",
        interacciones_medicamentosas="No tomar con alcohol",
    )
    data = {
        "id": medicamento.id,
        "nombre_comercial": medicamento.nombre_comercial,
        "nombre_generico": medicamento.nombre_generico,
        "ingredientes": medicamento.ingredientes,
        "concentracion": medicamento.concentracion,
        "forma_presentacion": medicamento.forma_presentacion,
        "forma_farmaceutica": medicamento.forma_farmaceutica,
        "via_administracion": medicamento.via_administracion,
        "indicaciones_terapeuticas": medicamento.indicaciones_terapeuticas,
        "contraindicaciones": medicamento.contraindicaciones,
        "efectos_secundarios": medicamento.efectos_secundarios,
        "instrucciones_dosificacion": medicamento.instrucciones_dosificacion,
        "fabricante": medicamento.fabricante,
        "informacion_almacenamiento": medicamento.informacion_almacenamiento,
        "interacciones_medicamentosas": medicamento.interacciones_medicamentosas,
    }

    serialized_data = MedicamentoSerializer(data=data)
    serialized_object = MedicamentoSerializer(medicamento)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_item_serializer():
    from maestro.serializers import ItemSerializer

    item = Item.objects.create(
        nombre="Respirador artificial",
        tipo=Item.Tipo.SOPORTE_VITAL,
    )
    data = {
        "id": item.id,
        "nombre": item.nombre,
        "tipo": item.tipo,
    }

    serialized_data = ItemSerializer(data=data)
    serialized_object = ItemSerializer(item)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_equipamiento_serializer():
    from maestro.serializers import EquipamientoSerializer

    equipamiento = Equipamiento.objects.create(item=Item.objects.all().first(), marca="HYUNDAI", modelo="SAMS1XY")
    data = {
        "id": equipamiento.id,
        "item": equipamiento.item.id,
        "marca": equipamiento.marca,
        "modelo": equipamiento.modelo,
    }

    serialized_data = EquipamientoSerializer(data=data)
    serialized_object = EquipamientoSerializer(equipamiento)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_quiebre_serializer():
    from maestro.serializers import QuiebreSerializer

    quiebre = Quiebre.objects.create(
        institucion=Institucion.objects.all().first(),
        medicamento=Medicamento.objects.all().first(),
        cantidad=10,
    )
    data = {
        "id": quiebre.id,
        "institucion": quiebre.institucion.id,
        "medicamento": quiebre.medicamento.id,
        "cantidad": quiebre.cantidad,
    }

    serialized_data = QuiebreSerializer(data=data)
    serialized_object = QuiebreSerializer(quiebre)
    serialized_data.is_valid()

    assert json.dumps(serialized_object.data) == json.dumps(data), "data serializada no tiene el orden correcto"
    assert (
        str(serialized_data.errors["non_field_errors"])
        == "[ErrorDetail(string='Los campos institucion, medicamento deben formar un conjunto único.', code='unique')]"
    ), f"Errores: {serialized_data.errors}"
