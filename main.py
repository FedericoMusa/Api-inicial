# Instalación: pip install fastapi uvicorn
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException

# Modelo de datos
class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    email: EmailStr

# Inicialización de FastAPI
app = FastAPI()

# Base de datos simulada con un array
persona_db = []
contador_id = 0  # Para asegurar IDs únicos

# Crear persona
@app.post("/personas/", response_model=Persona)
def crear_persona(persona: Persona):
    global contador_id
    persona.id = contador_id
    contador_id += 1
    persona_db.append(persona)
    return persona

# Ver persona por ID
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Listar todas las personas
@app.get("/personas/", response_model=list[Persona])
def listar_personas():
    return persona_db

# Actualizar persona
@app.put("/personas/{persona_id}", response_model=Persona)
def actualizar_persona(persona_id: int, persona: Persona):
    for index, p in enumerate(persona_db):
        if p.id == persona_id:
            persona_actualizada = Persona(id=persona_id, **persona.dict())
            persona_db[index] = persona_actualizada
            return persona_actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Eliminar persona
@app.delete("/personas/{persona_id}")
def eliminar_persona(persona_id: int):
    for index, p in enumerate(persona_db):
        if p.id == persona_id:
            del persona_db[index]
            return {"detail": f"Persona con ID {persona_id} eliminada"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")
