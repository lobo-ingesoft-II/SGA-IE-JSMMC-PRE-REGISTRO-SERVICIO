
# 📚 SGA-IE-JSMMC-PRE-REGISTRO-SERVICIO

**Autor:** Jhoan Sebastian Franco Ruiz

---
API o Servicio para la prematricula.

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

## 🔧 Endpoints REST

| Método | Endpoint                    | Descripción                                 |
|--------|-----------------------------|---------------------------------------------|
| GET    | `/pre_registration`         | Listar todos los registros de prematrícula  |
| GET    | `/pre_registration/{id}`    | Consultar un registro por ID                |
| GET    | `/pre_registration/getId/{numeroDocumentoEstudiante}`    | Consultar el ID de un resgistro por el numero de documneto                |
| POST   | `/pre_registration`         | Crear un nuevo registro de prematrícula     |
| DELETE | `/pre_registration/{id}`    | Borrar  un registro de prematrícula         |
| PUT    | `/pre_registration/{id}`    | Modificar todo un registro de prematricula  |
---

### Ejemplo de uso (POSTMAN)

**GET**
![imagen](/imagenes/POSTMAN-GET.png)

**POST**

![imagen](/imagenes/POSTMAN-POST1.png)
![imagen](/imagenes/POSTMAN-POST2.png)

**DELETE**
![imagen](/imagenes/POSTMAN-DELETE.png)

**PUT**
![imagen](/imagenes/POSTMAN-PUT.png)
--- 

### 📑 Swagger

La documentación Swagger está disponible en:
http://localhost:8010/docs
---

### ⚙️ Configuración !!!IMPORTANTE 
Crea un archivo .env en API_PRE_REGISTRO/ o un archivo justo por fuera de la app con el siguiente contenido:

Agrega la siguiente línea (reemplaza con tu URI real de MongoDB):

   ```
   MONGO_URI=mongodb+srv://usuario:contraseña@host.mongodb.net/tu_basededatos?retryWrites=true&w=majority
   ```

---
### 🚀 Instalación y Ejecución
Instala las dependencias:
```bash
pip install -r requirements.txt
```
Ejecuta el servidor:
```bash
uvicorn app.main:app --reload --port 8010
```

---
###  🚀 Correr pruebas unitarias

De forma global 
```bash
pytest app/test/unitTest_queryMongoDB.py
```

De forma mas especifica prueba <test_put_prematricula_invalid_id>
```bash
pytest app/test/unitTest_queryMongoDB.py::test_put_prematricula_invalid_id
```

---
### ¿Porque puerto 8010 para el servidor Uvicorn?
porque se va a llamar ahi para la peticion de la api de pdf. 


