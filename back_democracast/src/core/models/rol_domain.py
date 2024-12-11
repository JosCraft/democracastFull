from pydantic import BaseModel
from typing import Optional

class RolDomain(BaseModel):
    id: Optional[int]
    nombre: str
    
    