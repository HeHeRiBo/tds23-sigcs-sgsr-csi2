import pytest
from datetime import date
from django.db.utils import IntegrityError
from maestro.models import Institucion, Medicamento, Quiebre
from stock.models import Lote, Consumo, Stock, Movimiento


@pytest.mark.django_db
def test_lote_model():
    m = Medicamento.objects.all().first()
    fv = date(2024, 7, 10)
    lote = Lote(
        codigo="AU_PRMINC_100001_CL_CENABAST_20230710_20240816",
        medicamento=m,
        cantidad=500,
        fecha_vencimiento=fv,
    )
    lote.save()

    assert lote.codigo == "AU_PRMINC_100001_CL_CENABAST_20230710_20240816"
    assert lote.medicamento == m
    assert lote.cantidad == 500
    assert lote.fecha_vencimiento == fv

    assert str(lote) == lote.codigo, "se debe usar el código como representación str del objeto"

    lote.medicamento.delete()
    assert Lote.objects.filter(id=lote.id).first() is None, "eliminar medicamento debe eliminar lote en cascada"


@pytest.mark.django_db
def test_consumo_model():
    i = Institucion.objects.all().first()
    m = Medicamento.objects.all().first()
    f = date.today()

    consumo = Consumo(
        institucion=i,
        medicamento=m,
        cantidad=0,
    )
    consumo.save()

    assert consumo.institucion == i
    assert consumo.medicamento == m
    assert consumo.cantidad == 0
    assert consumo.fecha == f, "la fecha por defecto debe ser la del día en que se genera el consumo"

    consumo.cantidad = -500
    consumo.save()

    assert consumo.cantidad < 0, "consumo debe ser mayor o igual que cero"


@pytest.mark.django_db
def test_stock_model():
    q = Quiebre.objects.all().first()
    f = date.today()

    s = Stock(
        institucion=q.institucion,
        medicamento=q.medicamento,
    )
    s.save()

    assert s.institucion == q.institucion
    assert s.medicamento == q.medicamento
    assert s.cantidad == 0, "el stock inicial siempre debe ser cero"
    assert s.has_quiebre is False, "el stock inicial no debe tener quiebre"
    assert s.fecha_actualizacion == f, "la fecha de actualizacion es siempre la actual"

    _, created = Stock.objects.get_or_create(
        institucion=q.institucion,
        medicamento=q.medicamento,
    )
    assert not created, "institucion y medicamento deben ser unique together"


@pytest.mark.django_db
def test_movimiento_model():
    i = Institucion.objects.all().first()
    lote = Lote.objects.all().first()
    f = date.today()

    m = Movimiento(institucion=i, lote=lote)
    m.save()

    assert m.institucion == i
    assert m.lote == lote
    assert m.fecha == f, "la fecha por defecto debe ser la del día en que se genera el movimiento"

    with pytest.raises(IntegrityError) as exc_info:
        Movimiento.objects.create(institucion=i, lote=lote), "hola"
    assert str(exc_info.value) == "UNIQUE constraint failed: stock_movimiento.lote_id", "un lote no puede estar en más de una institución"
