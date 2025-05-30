from pydantic_settings import BaseSettings

# Configuración de la conexión a MongoDB usando Pydantic
class Settings(BaseSettings):
    mongo_uri: str

    class Config:
        env_file = ".env"

settings = Settings()

# Example usage 
# print(settings.mongo_uri)  