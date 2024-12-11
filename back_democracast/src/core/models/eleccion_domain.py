from pydantic import BaseModel
from typing import Optional
from datetime import date


class EleccionDomain(BaseModel):
    id: Optional[int]
    nombre: str
    fecha: date
    estado_id: str
    votospermitidos: int