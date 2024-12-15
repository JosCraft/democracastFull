from dataclasses import dataclass
@dataclass
class CandidatoDTOCreate:
    numero_cartelera: int
    cantidad_votos: int
    eleccion_id: int
    persona_id: int

@dataclass
class CandidatoDTOUpdate:
    numero_cartelera: int
    eleccion_id: int
    persona_id: int

@dataclass
class CandidatoDTOMostrar:
    id: int
    cantidad_votos: int