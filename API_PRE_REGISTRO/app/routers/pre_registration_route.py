from fastapi import APIRouter # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB



from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from app.schemas.form_pre_registro_schema import form_pre_registro # Importar el modelo de datos para validación

router = APIRouter() 

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

    # Obtener la colección de <prematriculas>
    pre_registration_collection = db["prematriculas"]

    # Obtener todos los documentos de la colección
    documents = list(pre_registration_collection.find())

    # Convertir los ObjectId a string para que sean serializables (Es decir evita errorres ya que JSON no puede entender ObjectId)
    for doc in documents:
        doc["_id"] = str(doc["_id"])

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

    pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

    try:
        objeto_Id = ObjectId(id) # Primero convertimos el id a ObjectId  porque MongoDB utiliza este tipo de dato para los identificadores únicos, Si no da error.
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")

    # Buscar el Objeto o documento por su ID
    document = pre_registration_collection.find_one({"_id": objeto_Id})

    # Convertir los ObjectId a string para que sean serializables (Es decir evita errorres ya que JSON no puede entender ObjectId)
    if document:
        document["_id"] = str(document["_id"])
        return {"documento": document}
    else:
        raise HTTPException(status_code=404, detail="Documento no encontrado")


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
    pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

    # Buscar documento por su numero Documento 
    document = pre_registration_collection.find_one({"numeroDocumento": numeroDocumentoEstudiante})

    if not document:    
        raise HTTPException(status_code=404, detail="Documento o numeroDocumento no encontrado")
    
    # Encontrar el id 
    idStudent =  str(document["_id"])

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
   
   # verificar que el documento tenga los campos necesarios 
   # No se hace porque el modelo PreRegistrationModel ya tiene los campos necesarios definidos y validados

    pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

    # Convertir el modelo a un diccionario
    document_dict = document.model_dump() # Convertir el modelo Pydantic a un diccionario

    # No es necesario crear un ObjectId manualmente, MongoDB lo genera automáticamente al insertar el documento con insert_one

    # Insertar el documento en la colección
    result = pre_registration_collection.insert_one(document_dict)

    # Convertir el ObjectId a string para que sea serializable
    document_dict["_id"] = str(result.inserted_id)

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
    pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

    try:
        objeto_Id = ObjectId(id)  # Convertir el id a ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")
    
    # Buscar el documento por su ID
    document = pre_registration_collection.find_one({"_id": objeto_Id})

    if not document:    
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    # Eliminar el documento
    pre_registration_collection.delete_one({"_id": objeto_Id})  
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
   # verificar que el documento tenga los campos necesarios 
   # No se hace porque el modelo PreRegistrationModel ya tiene los campos necesarios definidos y validados

    pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

    # Convertir el modelo a un diccionario
    document_dict = document.model_dump() # Convertir el modelo Pydantic a un diccionario

    try:
        objeto_Id = ObjectId(id)  # Convertir el id a ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")
    
    filter = {"_id": objeto_Id}

    # Hacer un remplazo con un filtro 
    resultado = pre_registration_collection.replace_one(filter, document_dict)

    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    
    # Si es correcto mandar un JSON con el resultado 
    return {"detail": "Documento actualizado Exitosamente"}









