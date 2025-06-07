# API_PRE_REGISTRO/app/backend/config.py

import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

# Construye la ruta absoluta a tu .env (tres niveles arriba)
env_path = Path(__file__).parents[3] / ".env"

# Carga variables al entorno
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    # Pydantic leerá MONGO_URI de las env vars
    mongo_uri: str = Field(..., env="MONGO_URI")

    class Config:
        env_file = env_path
        env_file_encoding = "utf-8"
        extra = "ignore"

# Instancia global para quien importe `settings`
settings = Settings()

# Constante para quien prefiera no usar Pydantic
MONGO_URI = settings.mongo_uri





#print("DEBUG settings.mongo_uri:", settings.mongo_uri)
# import os

# env_path = os.path.join(os.path.dirname(__file__), ".env")
# print("¿Existe .env?:", os.path.exists(env_path))
# if os.path.exists(env_path):
#     with open(env_path) as f:
#         print("Contenido de .env:")
#         print(f.read())


# print(settings.mongo_uri)  