from dataclasses import dataclass

@dataclass
class PersonaDTOCreate:
    nombre: str
    apellido: str
  
@dataclass
class PersonaDTOUpdate:
    nombre: str
    apellido: str
@dataclass
class PersonaDTOMostrar:
    nombre: str
    apellido: str
    
    