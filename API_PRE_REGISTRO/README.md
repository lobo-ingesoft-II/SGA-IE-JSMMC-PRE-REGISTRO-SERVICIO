
# 📚 SGA-IE-JSMMC-PRE-REGISTRO-SERVICIO

**Autor:** Jhoan Sebastian Franco Ruiz

---
API para la prematricula
Recepción y validación de datos del formulario de pre-matrícula
Almacenamiento de datos del acudiente y estudiante
Gestión del estado del trámite

Requisitos cubiertos:
RF1.1: Formulario de pre-matrícula
RF1.5: Inicio del trámite de matrícula

LLAMAR EN POWERSHELL
.\crear_fastapi_estructura.ps1

---

## 📝 Descripción general

API para la gestión del pre-registro de estudiantes y acudientes en la Institución Educativa Departamental Josué Manrique.  
Permite registrar, consultar y validar datos de pre-matrícula, almacenando la información en MongoDB y exponiendo endpoints REST documentados con Swagger/FastAPI.

---

## 🎯 Funcionalidades

- Recepción y validación de datos del formulario de pre-matrícula.
- Almacenamiento de datos del estudiante y acudientes.
- Consulta de registros existentes por ID o listado completo.
- Documentación interactiva con Swagger (FastAPI).

---

## 📁 Estructura del Proyecto

ESTRUCUTURA DE CARPETAS

```
    └── app/
        ├── backend/            # Backend functionality and configs
        |   ├── config.py           # Configuration settings
        │   └── session.py          # Database session manager
        ├── models/             # SQLAlchemy models
        │   ├── auth.py             # Authentication models
        |   ├── base.py             # Base classes, mixins
        |   └── ...                 # Other service models
        ├── routers/            # API routes
        |   ├── auth.py             # Authentication routers
        │   └── ...                 # Other service routers
        ├── schemas/            # Pydantic models - Models data validation
        |   ├── auth.py              
        │   └── ...
        ├── services/           # Business logic
        |   ├── auth.py             # Create user, generate and verify tokens
        |   ├── base.py             # Base classes, mixins
        │   └── ...
        ├── cli.py              # Command-line utilities
        ├── const.py            # Constants
        ├── exc.py              # Exception handlers
        └── main.py             # Application runner
```


---

## 🔧 Endpoints REST

| Método | Endpoint                    | Descripción                                 |
|--------|-----------------------------|---------------------------------------------|
| GET    | `/pre_registration`         | Listar todos los registros de prematrícula  |
| GET    | `/pre_registration/{id}`    | Consultar un registro por ID                |
| POST   | `/pre_registration`         | Crear un nuevo registro de prematrícula     |
| DELETE | `/pre_registration/{id}`    | Borrar  un registro de prematrícula     |
---

### Ejemplo de uso (POSTMAN)

**GET**
![imagen](/API_PRE_REGISTRO/imagenes/POSTMAN-GET.png)

**POST**

![imagen](/API_PRE_REGISTRO/imagenes/POSTMAN-POST1.png)
![imagen](/API_PRE_REGISTRO/imagenes/POSTMAN-POST2.png)

**DELETE**
![imagen](/API_PRE_REGISTRO/imagenes/POSTMAN-DELETE.png)


--- 
### 📑 Swagger

La documentación Swagger está disponible en:
http://localhost:8000/docs
---

### ⚙️ Configuración !!!IMPORTANTE 
Crea un archivo .env en API_PRE_REGISTRO/ o un archivo justo por fuera de la app con el siguiente contenido:

Agrega la siguiente línea (reemplaza con tu URI real de MongoDB):

   ```
   MONGO_URI=mongodb+srv://usuario:contraseña@host.mongodb.net/tu_basededatos?retryWrites=true&w=majority
   ```

---
🚀 Instalación y Ejecución
Instala las dependencias:
```bash
pip install -r requirements.txt
```
Ejecuta el servidor:
```bash
uvicorn app.main:app --reload
```
Accede a la documentación interactiva en http://localhost:8000/docs
