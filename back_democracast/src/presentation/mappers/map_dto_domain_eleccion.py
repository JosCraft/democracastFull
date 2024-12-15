from src.core.models.eleccion_domain import EleccionDomain
from src.presentation.dto.eleccion_dto import EleccionDTOCreate

def map_dto_eleccion(EleccionDTO: EleccionDTOCreate) -> EleccionDomain:
    return EleccionDomain(nombre=EleccionDTO.nombre, 
                           fecha=EleccionDTO.fecha, 
                           tipo_id=EleccionDTO.tipo_id
                           )
