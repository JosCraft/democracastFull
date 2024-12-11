from pydantic import BaseModel
from typing import Optional

class PersonaDomain(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    