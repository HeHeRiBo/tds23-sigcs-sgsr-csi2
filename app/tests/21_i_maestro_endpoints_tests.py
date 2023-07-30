import pytest
from maestro.models import Medicamento, Institucion


@pytest.mark.django_db
def test_add_medicamentos(client):
    response = client.post(
        "/maestro/medicamentos",
        {
            "nombre_comercial": "Panadol",
            "nombre_generico": "Paracetamol",
            "ingredientes": "Ácido Acetil Acetílico",
            "concentracion": "20 gr/kg",
            "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
            "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
            "via_administracion": Medicamento.Via.ORAL,
            "indicaciones_terapeuticas": "tome con abundante agua",
            "contraindicaciones": "no tomar estando embarazada",
            "efectos_secundarios": "dolor estomacal",
            "instrucciones_dosificacion": "1 tableta cada 6 horas",
            "fabricante": "SAVAL",
            "informacion_almacenamiento": "Guardar en un lugar fresco y oscuro",
            "interacciones_medicamentosas": "No tomar con alcohol",
        },
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["nombre_comercial"] == "Panadol"
    assert response.data["nombre_generico"] == "Paracetamol"
    assert response.data["ingredientes"] == "Ácido Acetil Acetílico"
    assert response.data["concentracion"] == "20 gr/kg"
    assert response.data["forma_presentacion"] == Medicamento.FormaPresentacion.FRASCO
    assert response.data["forma_farmaceutica"] == Medicamento.FormaFarmaceutica.TABLETAS
    assert response.data["via_administracion"] == Medicamento.Via.ORAL
    assert response.data["indicaciones_terapeuticas"] == "tome con abundante agua"
    assert response.data["contraindicaciones"] == "no tomar estando embarazada"
    assert response.data["efectos_secundarios"] == "dolor estomacal"
    assert response.data["instrucciones_dosificacion"] == "1 tableta cada 6 horas"
    assert response.data["fabricante"] == "SAVAL"
    assert response.data["informacion_almacenamiento"] == "Guardar en un lugar fresco y oscuro"
    assert response.data["interacciones_medicamentosas"] == "No tomar con alcohol"


@pytest.mark.django_db
def test_list_medicamentos(client):
    client.post(
        "/maestro/medicamentos",
        {
            "nombre_comercial": "Panadol",
            "nombre_generico": "Paracetamol",
            "ingredientes": "Ácido Acetil Acetílico",
            "concentracion": "20 gr/kg",
            "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
            "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
            "via_administracion": Medicamento.Via.ORAL,
            "indicaciones_terapeuticas": "tome con abundante agua",
            "contraindicaciones": "no tomar estando embarazada",
            "efectos_secundarios": "dolor estomacal",
            "instrucciones_dosificacion": "1 tableta cada 6 horas",
            "fabricante": "SAVAL",
            "informacion_almacenamiento": "Guardar en un lugar fresco y oscuro",
            "interacciones_medicamentosas": "No tomar con alcohol",

        },
        content_type="application/json",
    )
    response = client.get("/maestro/medicamentos", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) > 0, "se agregó más de un movimiento en la base de datos"


@pytest.mark.django_db
def test_get_medicamentos(client):
    client.post(
        "/maestro/medicamentos",
        {
            "nombre_comercial": "Panadol",
            "nombre_generico": "Paracetamol",
            "ingredientes": "Ácido Acetil Acetílico",
            "concentracion": "20 gr/kg",
            "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
            "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
            "via_administracion": Medicamento.Via.ORAL,
            "indicaciones_terapeuticas": "tome con abundante agua",
            "contraindicaciones": "no tomar estando embarazada",
            "efectos_secundarios": "dolor estomacal",
            "instrucciones_dosificacion": "1 tableta cada 6 horas",
            "fabricante": "SAVAL",
            "informacion_almacenamiento": "Guardar en un lugar fresco y oscuro",
            "interacciones_medicamentosas": "No tomar con alcohol",

        },
        content_type="application/json",
    )
    response = client.get("/maestro/medicamentos/36", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert response.data["id"] == 36, "no se obtuvieron movimientos"


@pytest.mark.django_db
def test_delete_medicamentos(client):
    client.post(
        "/maestro/medicamentos",
        {

            "nombre_comercial": "Panadol",
            "nombre_generico": "Paracetamol",
            "ingredientes": "Ácido Acetil Acetílico",
            "concentracion": "20 gr/kg",
            "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
            "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
            "via_administracion": Medicamento.Via.ORAL,
            "indicaciones_terapeuticas": "tome con abundante agua",
            "contraindicaciones": "no tomar estando embarazada",
            "efectos_secundarios": "dolor estomacal",
            "instrucciones_dosificacion": "1 tableta cada 6 horas",
            "fabricante": "SAVAL",
            "informacion_almacenamiento": "Guardar en un lugar fresco y oscuro",
            "interacciones_medicamentosas": "No tomar con alcohol",
        },
        content_type="application/json",
    )

    response = client.delete("/maestro/medicamentos/36", content_type="application/json")
    assert response.status_code == 204, "endpoint no encontrado"

    response = client.get("/maestro/medicamentos/36", content_type="application/json")
    assert response.status_code == 404, "el movimiento no fue eliminado"


@pytest.mark.django_db
def test_add_medicamento_invalid_json(client):
    response = client.post(
        "/maestro/medicamentos",
        {

            "id_nombre_comercial": "Panadol",
            "nombre_generico": "Paracetamol",
            "ingredientes": "Ácido Acetil Acetílico",
            "concentracion": "20 gr/kg",
            "forma_presentacion": Medicamento.FormaPresentacion.FRASCO,
            "forma_farmaceutica": Medicamento.FormaFarmaceutica.TABLETAS,
            "via_administracion": Medicamento.Via.ORAL,
            "indicaciones_terapeuticas": "tome con abundante agua",
            "contraindicaciones": "no tomar estando embarazada",
            "efectos_secundarios": "dolor estomacal",
            "instrucciones_dosificacion": "1 tableta cada 6 horas",
            "fabricante": "SAVAL",
            "informacion_almacenamiento": "Guardar en un lugar fresco y oscuro",
            "interacciones_medicamentosas": "No tomar con alcohol",
        },
        content_type="application/json",
    )
    assert response.status_code == 400, "endpoint no encontrado / no se debe permitir data mal formada"



@pytest.mark.django_db
def test_add_instituciones(client):
    response = client.post(
        "/maestro/instituciones",
        {
            "nombre": "Hospital felix bulnes de prado y ochagavia",
            "tipo": Institucion.Tipo.HOSPITAL,
            "titularidad": Institucion.Titularidad.PUBLICO,
            "num_camas_uti": 10,
            "num_camas_uci": 5,
            "factor": 0.5,
        },
        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["nombre"] == "Hospital felix bulnes de prado y ochagavia"
    assert response.data["tipo"] == Institucion.Tipo.HOSPITAL
    assert response.data["titularidad"] == Institucion.Titularidad.PUBLICO
    assert response.data["num_camas_uti"] == 10
    assert response.data["num_camas_uci"] == 5
    assert response.data["factor"] == 0.5


@pytest.mark.django_db
def test_list_instituciones(client):
    client.post(
        "/maestro/instituciones",
        {
            "nombre": "Hospital felix bulnes de prado y ochagavia",
            "tipo": Institucion.Tipo.HOSPITAL,
            "titularidad": Institucion.Titularidad.PUBLICO,
            "num_camas_uti": 10,
            "num_camas_uci": 5,
            "factor": 0.5,

        },
        content_type="application/json",
    )
    response = client.get("/maestro/instituciones", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) > 0, "se agregó más de un movimiento en la base de datos"


@pytest.mark.django_db
def test_get_instituciones(client):
    client.post(
        "/maestro/instituciones",
        {
            "nombre": "Hospital felix bulnes de prado y ochagavia",
            "tipo": Institucion.Tipo.HOSPITAL,
            "titularidad": Institucion.Titularidad.PUBLICO,
            "num_camas_uti": 10,
            "num_camas_uci": 5,
            "factor": 0.5,
        },
        content_type="application/json",
    )
    response = client.get("/maestro/instituciones/36", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert response.data["id"] == 36, "no se obtuvieron movimientos"


@pytest.mark.django_db
def test_delete_instituciones(client):
    client.post(
        "/maestro/instituciones",
        {
            "nombre": "Hospital felix bulnes de prado y ochagavia",
            "tipo": Institucion.Tipo.HOSPITAL,
            "titularidad": Institucion.Titularidad.PUBLICO,
            "num_camas_uti": 10,
            "num_camas_uci": 5,
            "factor": 0.5,
        },
        content_type="application/json",
    )

    response = client.delete("/maestro/instituciones/36", content_type="application/json")
    assert response.status_code == 204, "endpoint no encontrado"

    response = client.get("/maestro/instituciones/36", content_type="application/json")
    assert response.status_code == 404, "el movimiento no fue eliminado"


@pytest.mark.django_db
def test_add_institucion_invalid_json(client):
    response = client.post(
        "/maestro/instituciones",
        {

            "id_nombre": "Hospital felix bulnes de prado y ochagavia",
            "tipo": Institucion.Tipo.HOSPITAL,
            "titularidad": Institucion.Titularidad.PUBLICO,
            "num_camas_uti": 10,
            "num_camas_uci": 5,
            "factor": 0.5,
        },
        content_type="application/json",
    )
    assert response.status_code == 400, "endpoint no encontrado / no se debe permitir data mal formada"



@pytest.mark.django_db
def test_add_equipamientos(client):
    response = client.post(
        "/maestro/equipamientos",
        {"item": 1, "marca": "HYUNDAI", "modelo": "SAMS1XY"},

        content_type="application/json",
    )
    assert response.status_code == 201, "endpoint no encontrado"
    assert response.data["item"] == 1
    assert response.data["marca"] == "HYUNDAI"
    assert response.data["modelo"] == "SAMS1XY"



@pytest.mark.django_db
def test_list_equipamientos(client):
    client.post(
        "/maestro/equipamientos",

        {"item": 1, "marca": "HYUNDAI", "modelo": "SAMS1XY"},

        content_type="application/json",
    )
    response = client.get("/maestro/equipamientos", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert len(response.data) > 0, "se agregó más de un movimiento en la base de datos"


@pytest.mark.django_db
def test_get_equipamientos(client):
    client.post(
        "/maestro/equipamientos",
        {"item": 1, "marca": "HYUNDAI", "modelo": "SAMS1XY"},

        content_type="application/json",
    )
    response = client.get("/maestro/equipamientos/23", content_type="application/json")
    assert response.status_code == 200, "endpoint no encontrado"
    assert response.data["id"] == 23, "no se obtuvieron movimientos"


@pytest.mark.django_db
def test_delete_equipamientos(client):
    client.post(
        "/maestro/equipamientos",

        {"item": 1, "marca": "HYUNDAI", "modelo": "SAMS1XY"},
        content_type="application/json",
    )

    response = client.delete("/maestro/equipamientos/23", content_type="application/json")
    assert response.status_code == 204, "endpoint no encontrado"

    response = client.get("/maestro/equipamientos/23", content_type="application/json")
    assert response.status_code == 404, "el movimiento no fue eliminado"


@pytest.mark.django_db
def test_add_equipamiento_invalid_json(client):
    response = client.post(
        "/maestro/equipamientos",
        {"id_item": 1, "marca": "HYUNDAI", "modelo": "SAMS1XY"},
        content_type="application/json",
    )
    assert response.status_code == 400, "endpoint no encontrado / no se debe permitir data mal formada"

