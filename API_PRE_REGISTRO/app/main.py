from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.routers.pre_registration_route as pre_registration_route


# Instancia de FastAPI
app = FastAPI()

# Importar las rutas
app.include_router(pre_registration_route.router)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# if __name__ == '__main__':
#     app.run(debug=True)