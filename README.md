# 🛒 MELI Products API  
API RESTful desarrollada en **FastAPI**, siguiendo una **arquitectura monolítica modular de 3 capas**.  
Permite listar, filtrar y comparar productos desde un dataset local (sin base de datos), con control de errores integral y despliegue containerizado.

### Enlace repositorio 
- **https://github.com/DanTor07/MELI-API-Products**
---

# 🧱 Arquitectura del Proyecto

El diseño sigue una **arquitectura en tres capas internas**, que permite mantener separación de responsabilidades y facilidad de mantenimiento.

```text
app/
├── main.py → Capa de presentación (rutas y controladores HTTP)
├── services.py → Capa de negocio (reglas de comparación, filtrado)
├── repository.py → Capa de datos (lectura de productos JSON)
├── models.py → Modelos Pydantic para validación
├── errors.py → Manejo de errores y excepciones unificadas
└── data/products.json → Fuente de datos local
```
### Decisiones arquitectónicas clave
- **Monolito modular:** ideal para un backend simple y autocontenido.  
- **Validación automática con Pydantic:** garantiza tipos seguros y evita errores de datos.  
- **Control de errores centralizado:** todos los fallos se devuelven en formato uniforme JSON.  
- **Pruebas automatizadas:** validan la lógica de negocio, errores y flujos HTTP completos.  
- **Contenedorización total:** Docker y Docker Compose permiten ejecución reproducible en cualquier entorno.
---

## ⚙️ Pila Tecnológica

| Tecnología                 | Uso |
|----------------------------|-----|
| **Python 3.12**            | Lenguaje principal |
| **FastAPI**                | Framework backend asíncrono |
| **Uvicorn**                | Servidor ASGI de alto rendimiento |
| **Pydantic v2**            | Validación de modelos y tipos |
| **Pytest**       | Pruebas automatizadas |
| **Docker / Docker Compose** | Contenerización y orquestación |
| **GenAI (ChatGPT / Copilot)** | Asistencia en diseño, optimización y documentación |

---

## 🚀 Ejecución del Proyecto

### 🔹 Opción 1 – Docker Compose

**Archivo `docker-compose.yml`:**

```bash
   Ejecución:
   
   docker compose up
```
**Luego abre: http://localhost:8000/docs**

### 🔹 Opción 2 – Docker

**Construcción manual:**

```bash
   docker build -t dantor20/meli-products-api:latest .
   docker run -it --rm -p 8000:8000 dantor20/meli-products-api
```
**Luego abre: http://localhost:8000/docs**


### 🔹 Opción 3 – Local con Uvicorn
```bash
   uvicorn app.main:app --reload
```
**Luego abre: http://localhost:8000/docs**

## 🧩 Puntos Finales Principales

| Método | Endpoint              | Descripción                                             |
|--------|-----------------------|---------------------------------------------------------|
| GET    | `/api/health`         | Verifica el estado de la API                            |
| GET    | `/api/products`       | Lista productos, con filtros y paginación               |
| GET    | `/api/products/{id}`  | Devuelve el detalle de un producto                      |
| GET    | `/api/compare`        | Compara múltiples productos y genera resumen objetivo   |

### 🧪 Ejemplo de comparación

**Petición:**

```bash
   GET /api/compare?ids=P001&ids=P002&ids=P003
```

```json
{
  "count": 2,
  "products": [
    {
      "id": "P001",
      "product_name": "Wireless Bluetooth Headphones",
      "image_url": "https://meli-products.com/images/headphones.jpg",
      "description": "Noise-cancelling over-ear headphones with long battery life.",
      "price": 89.99,
      "rating": 4.6,
      "specifications": {
        "battery_life": "30 hours",
        "connectivity": "Bluetooth 5.0",
        "weight": "250g"
      }
    },
    {
      "id": "P010",
      "product_name": "Wireless Mouse",
      "image_url": "https://meli-products.com/images/wireless-mouse.jpg",
      "description": "Silent click ergonomic mouse with adjustable DPI.",
      "price": 24.99,
      "rating": 4.1,
      "specifications": {
        "dpi_range": "800–1600",
        "battery_type": "AA",
        "connectivity": "2.4GHz wireless"
      }
    }
  ],
  "differences": {
    "price": {
      "min": 24.99,
      "max": 89.99,
      "range": 65
    },
    "rating": {
      "min": 4.1,
      "max": 4.6,
      "range": 0.5
    },
    "specs_diff": {
      "battery_life": [
        "30 hours",
        null],
      "weight": [
        "250g",
        null],
      "connectivity": [
        "Bluetooth 5.0",
        "2.4GHz wireless"
      ],
      "dpi_range": [null, "800–1600"
      ],
      "battery_type": [null, "AA"
      ]
    }
  },
  "summary": {
    "best_price": "P010",
    "best_rating": "P001"
  }
}
```
## ⚡ Puntos Finales Principales

### Todos los errores se devuelven con formato JSON uniforme:


```json
{
  "error": {
    "code": 404,
    "type": "http_error",
    "message": "Not Found",
    "details": null
  }
}
```
## 🧪 Pruebas Automatizadas

**Ejecución de tests:**

```bash
   python -m pytest -v
```
### Cobertura:

- /api/health → estado del sistema

- /api/products → listado, filtros y paginación

- /api/products/{id} → búsquedas válidas e inválidas

- /api/compare → comparación entre múltiples productos

- Control de errores (400, 404, 422, 500)

---

## 🤖 Integración de GenAI y Herramientas Modernas

El desarrollo fue asistido con herramientas de **IA generativa** como **ChatGPT**, empleadas de manera estratégica para:

- Diseñar la arquitectura inicial del proyecto (3 capas y modularidad).  
- Generar y refinar *prompts* técnicos para construir funciones específicas.  
- Acelerar tareas repetitivas (como definición de modelos y endpoints).  
- Validar mejores prácticas de manejo de errores, Docker y testing.  
- Documentar el código y elaborar el README de manera clara y profesional.

## 👨‍💻 Autor

### Daniel Torres
