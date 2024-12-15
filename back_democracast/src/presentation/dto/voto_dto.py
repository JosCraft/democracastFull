from dataclasses import dataclass

@dataclass
class VotoDTOCreate:
    user_id: int
    eleccion_id: int
    candidato_id: int
    numero_votos: int
@dataclass
class VotoDTOUpdate:
    user_id: int
    eleccion_id: int
    candidato_id: int
    numero_votos: int
@dataclass
class VotoDTOMostrar:
    eleccion_id: int
    candidato_id: int
    numero_votos: int
    

