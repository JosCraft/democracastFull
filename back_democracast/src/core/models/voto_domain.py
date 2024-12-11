from pydantic import BaseModel
from typing import Optional


class VotoDomain(BaseModel):
    id: Optional[int]
    user_id: int
    eleccion_id: int
    candidato_id: int
    numero_votos: int
    