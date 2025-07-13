import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from bson import ObjectId

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.schemas.form_pre_registro_schema import form_pre_registro

from app.services.query_MongoDB import (
    getPrematriculas,
    getPrematricula_byId,
    getId_preRegistration_byStudentNumber,
    deletePreRegistration_byId,
    put_preRegistration,
    createPreRegistration,
)



def build_dummy_form_pre_registro():
    return form_pre_registro(
        apellidos="Franco",
        nombres="Juan ",
        tipoDocumento="Tarjeta de Identidad",
        numeroDocumento="1234567890",
        fechaNacimiento="2010-05-15",
        paisNacimiento="COLOMBIA",
        departamentoNacimiento="CUNDINAMARCA",
        municipioNacimiento="Yopal",
        categoriaSisben="A",
        subcategoriaSisben="A2",
        direccionResidencia="Calle 10 #5-20",
        telefono="3201234567",
        rutaEscolar="Ruta 1",
        seguroMedico="Nueva EPS",
        discapacidad="NO",
        detalleDiscapacidad="",
        poblacionDesplazada="NO",
        fechaDesplazamiento="",
        paisResidencia="COLOMBIA",
        departamentoResidencia="CUNDINAMARCA",
        municipioResidencia="Yopal",
        gradoIngreso="6",
        institucionAnterior="Colegio ABC",
        municipioAnterior="Yopal",
        sede="INSTITUCIÓN EDUCATIVA DEPARTAMENTAL JOSUÉ MANRIQUE",
        acudiente1Parentesco="Padre",
        acudiente1Apellidos="Pérez Rodríguez",
        acudiente1Nombres="Carlos Alberto",
        acudiente1CC="987654321",
        acudiente1Celular="3109876543",
        acudiente1Ocupacion="Ingeniero",
        acudiente2Parentesco="Madre",
        acudiente2Apellidos="Gómez Ruiz",
        acudiente2Nombres="María Fernanda",
        acudiente2CC="1122334455",
        acudiente2Celular="3112233445",
        acudiente2Ocupacion="Docente"
    )

# Mock del documento de entrada
class DummyPreRegistro(form_pre_registro):
    def model_dump(self):
        return build_dummy_form_pre_registro()

@pytest.fixture
def mock_db(mocker):
    return mocker.patch("app.backend.session.db")

# TEST Para obtener prematriculas
def test_get_prematriculas(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.find.return_value = [{"_id": ObjectId(), "nombre": "Juan"}]

    docs = getPrematriculas()

    assert isinstance(docs, list)
    assert "_id" in docs[0]
    assert isinstance(docs[0]["_id"], str)


# TEST Para obtener pre-matricula por id valido 
@patch("app.services.query_MongoDB.db")  # 👈 Este es el db que importa tu función
def test_get_prematricula_by_id_valid(mock_db):
    collection = mock_db.__getitem__.return_value
    oid = ObjectId()
    expected_document = {"_id": oid, "nombre": "Juan"}

    collection.find_one.return_value = expected_document

    result = getPrematricula_byId(str(oid))

    assert result["_id"] == str(oid)
    assert result["nombre"] == "Juan"



# TEST Para obtener pre-matricula por id invalido
def test_get_prematricula_by_id_invalid():
    with pytest.raises(HTTPException) as exc:
        getPrematricula_byId("id_invalido")

    assert exc.value.status_code == 400


# TEST Para obtener pre-matricula pero id no encontrado 
def test_get_prematricula_by_id_not_found(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.find_one.return_value = None

    with pytest.raises(HTTPException) as exc:
        getPrematricula_byId(str(ObjectId()))

    assert exc.value.status_code == 404


# TEST para obetener el id de una preRegistro por NumeroEstudiante (encontrado)
@patch("app.services.query_MongoDB.db")  # 👈 Este es el db que importa tu función
def test_get_id_by_student_number_found(mock_db):
    collection = mock_db.__getitem__.return_value
    oid = ObjectId()
    collection.find_one.return_value = {"_id": oid}

    # Parchear nombre de variable incorrecta
    global numeroDocumentoEstudiante
    numeroDocumentoEstudiante = "1234567890"

    result = getId_preRegistration_byStudentNumber("123456789")
    assert result == str(oid)


# TEST para obetener el id de un preRegistro por NumeroEstudiante (No encontrado)
def test_get_id_by_student_number_not_found(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.find_one.return_value = None

    global numeroDocumentoEstudiante
    numeroDocumentoEstudiante = "123456789"

    with pytest.raises(HTTPException) as exc:
        getId_preRegistration_byStudentNumber("123456789")

    assert exc.value.status_code == 404


# TEST para borrar la preMatricula Valido
@patch("app.services.query_MongoDB.db")  # 👈 Este es el db que importa tu función
def test_delete_prematricula_valid(mock_db):
    collection = mock_db.__getitem__.return_value
    oid = ObjectId()
    collection.find_one.return_value = {"_id": oid}

    result = deletePreRegistration_byId(str(oid))
    assert result is True

# TEST para borrar la preMatricula Invalido
def test_delete_prematricula_invalid():
    with pytest.raises(HTTPException) as exc:
        deletePreRegistration_byId("id_invalido")

    assert exc.value.status_code == 400


# TEST para borrar la preMatricula no Encontrado
def test_delete_prematricula_not_found(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.find_one.return_value = None

    with pytest.raises(HTTPException) as exc:
        deletePreRegistration_byId(str(ObjectId()))

    assert exc.value.status_code == 404

# TEST para actualizar preMatricula exito
@patch("app.services.query_MongoDB.db")  # 👈 Este es el db que importa tu función
def test_put_prematricula_success(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.replace_one.return_value.matched_count = 1

    dummy = build_dummy_form_pre_registro()
    result = put_preRegistration(dummy, str(ObjectId()))
    assert result is True


# TEST para actualizar preMatricula NO exito
@patch("app.services.query_MongoDB.db")  # 👈 Este es el db que importa tu función
def test_put_prematricula_not_found(mock_db):
    collection = mock_db.__getitem__.return_value
    collection.replace_one.return_value.matched_count = 0

    with pytest.raises(HTTPException) as exc:
        dummy = build_dummy_form_pre_registro()
        put_preRegistration(dummy, str(ObjectId()))

    assert exc.value.status_code == 404

# TEST para actualizar preMatricula id No encontrado 
def test_put_prematricula_invalid_id():
    with pytest.raises(HTTPException) as exc:
        dummy = build_dummy_form_pre_registro()
        put_preRegistration(dummy, "id_invalido")

    assert exc.value.status_code == 400


# TEST para crear prematricula exito 
@patch("app.services.query_MongoDB.db")  # 👈 Importa db desde donde lo usa tu función
def test_create_prematricula(mock_db):
    collection = mock_db.__getitem__.return_value
    oid = ObjectId()  # este será el ID simulado
    collection.insert_one.return_value.inserted_id = oid  # lo forzamos como retorno

    dummy = build_dummy_form_pre_registro()
    result = createPreRegistration(dummy)

    assert result["_id"] == str(oid)  # debe coincidir

