from src.core.models.estado_domain import EstadoDomain
from src.presentation.dto.estado_dto import EstadoDTOCreate

def map_dto_estado(EstadoDTO: EstadoDTOCreate) -> EstadoDomain:
    return EstadoDomain(nombre=EstadoDTO.nombre, 
                        )