from src.core.models.usuario_domain import UsuarioDomain
from src.presentation.dto.usuario_dto import UsuarioDTOCreate

def map_dto_usuario(UsuarioDTO: UsuarioDTOCreate) -> UsuarioDomain:
    return UsuarioDomain(usuario=UsuarioDTO.usuario, 
                         password=UsuarioDTO.password, 
                         rol_id=UsuarioDTO.rol_id
                         )
