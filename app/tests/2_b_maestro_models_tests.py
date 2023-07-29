import pytest
from django.db.utils import IntegrityError
from django.db import models
from maestro.models import Item, Institucion, Medicamento


@pytest.mark.django_db
def test_institucion_model():
    from maestro.models import Institucion
    

    institucion = Institucion.objects.create(
        nombre="Hospital felix bulnes de prado y ochagavia",
        tipo=Institucion.Tipo.HOSPITAL,
        titularidad=Institucion.Titularidad.PUBLICO,
        num_camas_uti=10,
        num_camas_uci=5,
        factor=0.5,
    )
    
    assert institucion.tipo == Institucion.Tipo.HOSPITAL, "El tipo elegido debe estar dentro de la lista"
    assert institucion.titularidad == Institucion.Titularidad.PUBLICO, "La titularidad elegida debe estar dentro de la lista"    
    assert len(institucion.nombre) <= 255, "El largo máximo del nombre es 255 carácteres" 
    
    factor = Institucion._meta.get_field('factor')
    assert isinstance(factor, models.FloatField), "El campo debe ser Float"

    assert str(institucion) == institucion.nombre, "se debe usar el nombre de la institución como la representación str del objeto"

 
    institucion.num_camas_uci = -5
    institucion.num_camas_uti = -5
    with pytest.raises(IntegrityError):
        institucion.save()

        institucion = Institucion.objects.get(id=institucion.id)
        assert institucion.num_camas_uci >= 0, "Número de camas UCI debe ser mayor o igual que cero"
        assert institucion.num_camas_uti >= 0, "Número de camas UTI debe ser mayor o igual que cero"


@pytest.mark.django_db
def test_medicamento_model():
    from maestro.models import Medicamento
    

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

    assert medicamento.forma_presentacion == Medicamento.FormaPresentacion.FRASCO, "La forma de presentación elegida debe estar dentro de la lista"
    assert medicamento.forma_farmaceutica == Medicamento.FormaFarmaceutica.TABLETAS, "La forma farmacéutica elegida debe estar dentro de la lista"
    assert medicamento.via_administracion == Medicamento.Via.ORAL, "La vía de administración elegida debe estar dentro de la lista"

    assert str(medicamento) == f"{medicamento.nombre_comercial} ({medicamento.nombre_generico}) | {medicamento.fabricante}", "se debe usar la concatenación como representación str del objeto"

@pytest.mark.django_db
def test_item_model():
    from maestro.models import Item
    

    item = Item.objects.create(
        nombre="Respirador artificial",
        tipo=Item.Tipo.SOPORTE_VITAL,
    )

    assert item.tipo == Item.Tipo.SOPORTE_VITAL, "El item elegido debe estar dentro de la lista"
    assert str(item) == f"{item.nombre} ({item.tipo})",  "se debe usar la concatenación como representación str del objeto"


@pytest.mark.django_db
def test_equipamiento_model():
    from maestro.models import Equipamiento
    
    item = Item.objects.all().first() 

    equipamiento = Equipamiento.objects.create(
        item=item,
        marca="HYUNDAI",
        modelo="SAMS1XY"
    )

    assert equipamiento.item == item
    assert str(equipamiento) == f"{equipamiento.modelo} ({equipamiento.modelo}) | {equipamiento.item}",  "se debe usar la concatenación como representación str del objeto"

    equipamiento.item.delete()
    assert Item.objects.filter(id=equipamiento.id).first() is None, "eliminar item debe eliminar equipamiento en cascada"


@pytest.mark.django_db
def test_quiebre_model():
    from maestro.models import Quiebre

    institucion = Institucion.objects.all().first() 
    medicamento = Medicamento.objects.all().first()

    quiebre = Quiebre.objects.create(
        institucion=institucion,
        medicamento=medicamento,
        cantidad=10,
    )

    assert quiebre.institucion == institucion
    assert quiebre.medicamento == medicamento
    assert quiebre.cantidad >= 0, "La cantidad debe ser positiva"

    with pytest.raises(IntegrityError) as exc_info:
        Quiebre.objects.create(institucion=institucion, medicamento=medicamento, cantidad=10)
    assert str(exc_info.value) == "UNIQUE constraint failed: maestro_quiebre.institucion_id, maestro_quiebre.medicamento_id", "no puede haber más de un registro por institución, medicamente"
