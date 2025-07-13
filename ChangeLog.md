# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
y este proyecto sigue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Pruebas unitarias iniciales.
- Observabilidad con Prometheus Client.
- Rutas `PUT` y `GET` por número de documento.
- Archivo `.env` y configuración inicial de la base de datos.
- Gitflow branch policy (`gitflow-branch-policy.yml`).

### Changed
- Refactorización de rutas (`routes`).
- Actualización del archivo `README.md`.

### Removed
- Archivo `test_connection.py`.

---

## [1.0.0] - 2025-05-29

### Added
- Estructura inicial del proyecto y ejecutable en PowerShell.
- Primer archivo `README.md`.

---

## [1.1.0] - 2025-05-31

### Added
- Funcionalidad básica: conexión con la base de datos funcionando.
- Rutas `GET`, `POST`, y `DELETE` para completar CRUD.

### Changed
- Archivos reorganizados en nuevas carpetas.
- Documentación mejorada en `README.md`.

---

## [1.2.0] - 2025-06-07

### Added
- Rutas adicionales: `PUT` y `GET` por número de documento.

---

## [1.3.0] - 2025-07-06

### Added
- Integración de Prometheus para métricas de observabilidad.

---

## [1.4.0] - 2025-07-10

### Added
- Política de ramas Git (`gitflow-branch-policy.yml`).

---

## [1.5.0] - 2025-07-13

### Added
- Pruebas unitarias automatizadas.
- Creacion de (`changeLog.md`)

### Changed
- Refactorización de rutas (`routes`).
- Mejora en la documentación (`README.md`).
