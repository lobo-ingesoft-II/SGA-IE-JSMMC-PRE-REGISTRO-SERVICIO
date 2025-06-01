from fastapi import APIRouter 
from app.backend.session import db 


router = APIRouter() 

@router.get("/pre_registration")
def pre_registration(): 
    # Obtener la colección de <prematriculas>
    pre_registration_collection = db["prematriculas"]

    # Obtener todos los documentos de la colección
    documents = list(pre_registration_collection.find())

    # Convertir los ObjectId a string para que sean serializables
    for doc in documents:
        doc["_id"] = str(doc["_id"])
    return {"coleccion": documents}