from dataclasses import dataclass

@dataclass
class UsuarioDTOLogin:
    usurio: str
    password: str
    
@dataclass
class UsuarioDTOCreate:
    usuario: str
    password: str
    rol_id: int