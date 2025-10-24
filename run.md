# ▶️ Instrucciones de ejecución – MELI API Products

Proyecto backend desarrollado en **FastAPI**, con contenedor Docker y pruebas automatizadas.

---

## 🧱 Requisitos previos
- Python 3.12 o superior  
- Docker y Docker Compose
- Git

---

## 🔹 Opción 1 – Docker Compose

### 1️⃣ Archivo `docker-compose.yml`:

```bash
   Ejecución:
   
   docker compose up
```
**Abrir en el navegador: http://localhost:8000/docs**

## 🔹 Opción 2 – Docker

### 1️⃣ Construir la imagen
```bash
   docker build -t dantor20/meli-products-api:latest .
   docker run -it --rm -p 8000:8000 dantor20/meli-products-api
```
**Abrir en el navegador: http://localhost:8000/docs**

## 🔹 Opción 3 – Ejecución local (Uvicorn)

### 1️⃣ Crear entorno virtual e instalar dependencias
```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
```
### 2️⃣ Ejecutar la aplicación
```bash
   uvicorn app.main:app --reload
```
**Abrir en el navegador: http://localhost:8000/docs**