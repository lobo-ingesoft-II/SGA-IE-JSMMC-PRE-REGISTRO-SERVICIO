# SGA-IE-JSMMC-PRE-REGISTRO-SERVICIO

API para la prematricula
Recepción y validación de datos del formulario de pre-matrícula
Almacenamiento de datos del acudiente y estudiante
Gestión del estado del trámite

Requisitos cubiertos:
RF1.1: Formulario de pre-matrícula
RF1.5: Inicio del trámite de matrícula

LLAMAR EN POWERSHELL
.\crear_fastapi_estructura.ps1


ESTRUCUTURA DE CARPETAS
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