from pydantic import BaseModel
from typing import Optional


class CandidatoDomain(BaseModel):
    id: Optional[int]
    numero_cartelera: int
    cantidad_votos: int
    eleccion_id: int
    persona_id: int
    