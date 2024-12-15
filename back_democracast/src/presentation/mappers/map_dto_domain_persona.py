from src.core.models.persona_domain import PersonaDomain
from src.presentation.dto.persona_dto import PersonaDTOCreate

def map_dto_persona(PersonaDTO: PersonaDTOCreate) -> PersonaDomain:
    return PersonaDomain(nombre=PersonaDTO.nombre, 
                         apellido=PersonaDTO.apellido, 
                         dni=PersonaDTO.dni, 
                         fecha_nacimiento=PersonaDTO.fecha_nacimiento, 
                         genero_id=PersonaDTO.genero_id
    )
