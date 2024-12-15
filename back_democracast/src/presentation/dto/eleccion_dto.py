from dataclasses import dataclass

@dataclass
class EleccionDTOCreate:
    nombre: str
    fecha: date
    estado_id: str
    votospermitidos: int

@dataclass
class EleccionDTOUpdate:
    nombre: str
    fecha: date
    estado_id: str
    votospermitidos: int

@dataclass
class EleccionDTOMostrar:
    nombre: str
    fecha: date
    estado_id: str
    votospermitidos: int
    