from pydantic import BaseModel
from typing import Optional

class EstadoDomain(BaseModel):
    id: Optional[int]
    estado: str
    