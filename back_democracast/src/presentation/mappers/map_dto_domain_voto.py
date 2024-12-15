from src.core.models.voto_domain import VotoDomain
from src.presentation.dto.voto_dto import VotoDTOCreate

def map_dto_voto(VotoDTO: VotoDTOCreate) -> VotoDomain:
    return VotoDomain(usuario_id=VotoDTO.usuario_id, 
                      eleccion_id=VotoDTO.eleccion_id, 
                      candidato_id=VotoDTO.candidato_id
                      )
