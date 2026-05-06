from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuariosSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str= Field(min_length=8)

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class TareaSchems(BaseModel):
    titulo: str = Field(min_length=1,max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"   


class UsuarioAlta(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class UsuarioFormSchema(BaseModel):
    # Campos que se piden en el formulario, con validaciones específicas
    nombre: str = Field(min_length=2, max_length=30)
    apellido: str = Field(min_length=8, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8)
    telefono: Optional[str] = Field(None, min_length=10, max_length=15)
    foto: Optional[str] = None  # URL o ruta de la foto del usuario

    # Campos que no se piden en el formulario, pero son necesarios a la hora de agregar al usuario en base de datos
    activo: bool = True
    fecha_registro: datetime = Field(default_factory=datetime.now)
    ultimo_ingreso: datetime = Field(default_factory=datetime.now)
