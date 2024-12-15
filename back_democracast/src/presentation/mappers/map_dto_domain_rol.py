from src.core.models.rol_domain import RolDomain
from src.presentation.dto.rol_dto import RolDTOCreate

def map_dto_rol(RolDTO: RolDTOCreate) -> RolDomain:
    return RolDomain(nombre=RolDTO.nombre)
