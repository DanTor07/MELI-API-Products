# 🤖 Prompts usados

**Prompts utilizados en el desarrollo del proyecto**

Este documento recopila los principales prompts empleados con herramientas de **IA generativa (ChatGPT)** durante el desarrollo del proyecto.  
Cada uno fue diseñado de forma intencional para optimizar una etapa específica del flujo de trabajo: diseño, codificación, documentación y pruebas.

---

## 🧠 1. Diseño de arquitectura inicial

**Objetivo:**  
Definir la estructura técnica del proyecto, incluyendo las capas internas, la organización de archivos y la elección de tecnologías.

**Prompt:**
> "Crea una API REST con FastAPI usando una arquitectura limpia y tres capas en un monolito modular. No uses base de datos; persiste en JSON local.
Entrega un esqueleto mínimo, con archivos y nombres claros; evita scaffolding innecesario.
Incluye un CRUD simple y valida campos básicos.
Muestra primero el árbol del proyecto.
Aplica buenas prácticas (docstrings breves, manejo de errores y status HTTP razonables)"

---

## 💾 2. Generación del dataset (mock data en JSON)

**Objetivo:**  
Crear un archivo `products.json` realista y bien estructurado para simular datos de producto.

**Prompt:**
> "Genera un objeto JSON array de 10 productos. Este JSON se utilizará como datos de prueba (mock data) para el endpoint de una API desarrollada en FastAPI.  
> Requisitos del schema:  
> 1. El JSON debe ser un array ([]) conteniendo objetos.  
> 2. Cada objeto producto debe tener estrictamente los siguientes campos, en este orden:  
> - id (string)  
> - nombre_producto (string)  
> - url_imagen (string, URL de imagen válida de ejemplo)  
> - descripcion (string, breve y concisa)  
> - precio (float, con dos decimales)  
> - calificacion (float, entre 1.0 y 5.0)  
> - especificaciones (object/diccionario, con al menos 3 pares clave-valor relevantes al producto)  
> 
> **Importante: Todos los nombres de los campos dentro de los objetos del array deben estar en inglés."**

---

## ⚙️ 3. Creación del Dockerfile

**Objetivo:**  
Definir la contenedorización del proyecto, asegurando que pudiera ejecutarse en cualquier entorno.

**Prompt:**
> "Genera un Dockerfile minimalista para una app FastAPI en Python 3.12. Define como comando por defecto Uvicorn sirviendo app.main:app enlazado a 0.0.0.0:8000."
---

## 🧩 4. Creación de docker-compose.yml

**Objetivo:**  
Simplificar la ejecución y orquestación del contenedor.

**Prompt:**
> "Crea un archivo docker-compose.yml para levantar el servicio de la API que ya tiene imagen publicada en Docker Hub. El servicio debe llamarse 'api', exponer el puerto 8000, reiniciarse automáticamente y permitir ejecución con un solo comando (`docker compose up`)."
---

## 🧪 5. Generación de pruebas automatizadas

**Objetivo:**  
Validar todo el flujo de la API con `pytest` y `fastapi.testclient`.

**Prompt:**
> "Genera una suite de tests con Pytest para FastAPI que valide:  
> - `/api/health`  
> - `/api/products` con filtros  
> - `/api/products/{id}`  
> - `/api/compare` con dos y múltiples productos  
> - errores 404, 400, 422 y 500.  
> Los tests deben verificar estructura JSON, status codes y contenido de respuesta."


---

## 📘 6. Generación del README en formato Markdown

**Objetivo:**  
Redactar un `README.md` profesional, con secciones formateadas correctamente para Markdown.

**Prompt:**
> "Devuélveme cada parte de este texto de forma independiente.  
> Asegúrate de que cada sección, incluyendo títulos, listas y los ejemplos de código (como el YAML y JSON), esté formateada usando la sintaxis de Markdown / TEXT.  
> El objetivo es que la salida sea un archivo README.md legible, sin que ninguna parte quede como texto plano normal."

---

## 🧠 7. Prompt de mejora iterativa de prompts

**Objetivo:**  
Refinar los prompts usados para obtener resultados más precisos y útiles.

**Prompt:**
> "Mejora la calidad de este prompts técnicos para que las respuestas sean más concretas y adaptadas al contexto del proyecto. Evalúa y sugiere mejoras de estructura y precisión."

---
