from pydantic import BaseModel
from typing import Optional


class UsuarioDomain(BaseModel):
    id: Optional[int] = None
    usuario: str
    password: str
    rol_id: int
    estado_id: Optional[int] = None
    