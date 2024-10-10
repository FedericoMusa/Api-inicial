# FASTAPI 
# pip install fastapi uvicorn
from typing import Optional, List
from pydantic import BaseModel, EmailStr

class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    email: EmailStr

# API
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada con un array
persona_db = []

# Crear persona
@app.post("/personas/", response_model=Persona)
def crear_persona(persona: Persona):
    persona.id = len(persona_db)
    persona_db.append(persona)
    return persona

# Ver persona por ID
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Listar personas
@app.get("/personas/", response_model=List[Persona])
def listar_personas():
    return persona_db

# Actualizar persona (no implementado)
@Actualizar
# Eliminar persona (no implementado)


