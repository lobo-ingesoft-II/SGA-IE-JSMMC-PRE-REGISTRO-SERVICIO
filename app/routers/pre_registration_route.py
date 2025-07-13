from fastapi import APIRouter, Request # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB



from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from app.schemas.form_pre_registro_schema import form_pre_registro # Importar el modelo de datos para validación

# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from prometheus_client import CollectorRegistry, generate_latest

# imporar las consultas 
from app.services.query_MongoDB import getPrematriculas, getPrematricula_byId, getId_preRegistration_byStudentNumber, deletePreRegistration_byId, put_preRegistration, createPreRegistration

router = APIRouter() 

# Metricas 
REQUEST_COUNT_PRE_REGISTRATION_ROUTERS = Counter(
    "http_requests_total", 
    "TOTAL PETICIONES HTTP router-pre_registration",
    ["method", "endpoint"]
)

REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS = Histogram(
    "http_request_duration_seconds", 
    "DURACION DE LAS PETICIONES router-pre_registration",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]  
)

# 3. Errores por endpoint
ERROR_COUNT_PRE_REGISTRATION_ROUTERS = Counter(
    "http_request_errors_total",
    "TOTAL ERRORES HTTP (status >= 400)",
    ["endpoint", "method", "status_code"]
)

# Ruta para observabilidad 
@router.get("/custom_metrics")
def custom_metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT_PRE_REGISTRATION_ROUTERS)
    registry.register(REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS)
    registry.register(ERROR_COUNT_PRE_REGISTRATION_ROUTERS)
    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)

# GET /pre_registration
@router.get("/pre_registration" ,response_model=dict,
    responses={
        200: {
            "description": "Lista de documentos obtenida exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "coleccion": [
                            {
                                "_id": "6838ab661efa82c1dca6d3ed",
                                "apellidos": "Pérez Gómez",
                                "nombres": "Juan Carlos",
                                "...otros": "campos..."
                            }
                        ]
                    }
                }
            }
        },
        500: {
            "description": "Error interno al obtener los documentos",
            "content": {
                "application/json": {
                    "example": {"error": "Error interno del servidor"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def pre_registration(): 

    documents = getPrematriculas()
    return {"coleccion": documents}


# GET /pre_registration/{id}
@router.get(
    "/pre_registration/{id}",
    responses={
        200: {
            "description": "Documento encontrado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "documento": {
                            "_id": "6838ab661efa82c1dca6d3ed",
                            "apellidos": "Pérez Gómez",
                            "nombres": "Juan Carlos"
                            # ...otros campos...
                        }
                    }
                }
            }
        },
        400: {
            "description": "ID inválido",
            "content": {
                "application/json": {
                    "example": {"detail": "ID inválido, error: ..."}
                }
            }
        },
        404: {
            "description": "Documento no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento no encontrado"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def get_pre_registration(id: str):
    return {"documento": getPrematricula_byId(id)}

# GET /pre_registration/getId/{numeroDocumentoEstudiante}
@router.get("/pre_registration/getId/{numeroDocumentoEstudiante}" ,response_model=dict,
    responses={
        200: {
            "description": "ID encontrado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id_": "6838ab661efa82c1dca6d3ed",
                        "numeroDocumentoEstudiante": "1234567890"
                    }
                }
            }
        },
        404: {
            "description": "Documento o numeroDocumento no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento o numeroDocumento no encontrado"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def getId_pre_registration(numeroDocumentoEstudiante: str):

    idStudent = getId_preRegistration_byStudentNumber(numeroDocumentoEstudiante)
    
    # pasar el id en formato JSON
    return {"id_": idStudent,
            "numeroDocumentoEstudiante": numeroDocumentoEstudiante }


# POST /pre_registration
@router.post(
    "/pre_registration",
    # response_model=form_pre_registro,  # Asegúrate de que este modelo esté definido correctamente
    responses={
        201: {
            "description": "Documento creado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "_id": "6838ab661efa82c1dca6d3ed",
                        "apellidos": "Pérez Gómez",
                        "nombres": "Juan Carlos"
                        # ...otros campos...
                    }
                }
            }
        },
        400: {
            "description": "Error al crear el documento",
            "content": {
                "application/json": {
                    "example": {"detail": "Error al crear el documento"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def create_pre_registration(document:form_pre_registro):
   
    document_dict = createPreRegistration(document)
    return document_dict  # Retornar el documento creado con su ID asignado por MongoDB

#DELETE "/pre_registration/{id}"
@router.delete(
    "/pre_registration/{id}",
    responses={
        200: {
            "description": "Documento eliminado exitosamente",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento eliminado exitosamente"}
                }
            }
        },
        400: {
            "description": "ID inválido",
            "content": {
                "application/json": {
                    "example": {"detail": "ID inválido, error: ..."}
                }
            }
        },
        404: {
            "description": "Documento no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento no encontrado"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def delete_pre_registration(id: str):
    delete = deletePreRegistration_byId(id)
    if delete: 
        return {"detail": "Documento eliminado exitosamente"}


# PUT "/pre_registration/{id}"
# Es un remplazo de un archivo ya existente
@router.put("/pre_registration/{id}",
    responses={
        200: {
            "description": "Documento actualizado exitosamente",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento actualizado Exitosamente"}
                }
            }
        },
        400: {
            "description": "ID inválido",
            "content": {
                "application/json": {
                    "example": {"detail": "ID inválido, error: ..."}
                }
            }
        },
        404: {
            "description": "Documento no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Documento no encontrado"}
                }
            }
        }
    },
    tags=["Pre_Registration"]
)
def change_pre_registration(document:form_pre_registro, id: str):

    changePreRegistration = put_preRegistration(document, id)
    if changePreRegistration:

        # Si es correcto mandar un JSON con el resultado 
        return {"detail": "Documento actualizado Exitosamente"}









