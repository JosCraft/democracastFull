from src.core.models.candidato_domain import CandidatoDomain
from src.presentation.dto.candidato_dto import CandidatoDTOCreate

def map_dto_candidato(CandidatoDTO: CandidatoDTOCreate) -> CandidatoDomain:
    return CandidatoDomain(nombre=CandidatoDTO.nombre, 
                            apellido=CandidatoDTO.apellido, 
                            partido_id=CandidatoDTO.partido_id
                            )
