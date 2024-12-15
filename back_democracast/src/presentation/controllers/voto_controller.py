from fastapio import APIRouter, Depends, HTTPException, status

from src.core.services.voto_service import IVotoService
from src.core.dependency_inyection.dependency_inyection import build_voto_service
from src.presentation.dto.voto_dto import VotoDTOCreate, VotoDTOUpdate
from src.presentation.mappers.map_dto_domain_voto import map_dto_voto


voto_router = APIRouter(prefix="/api/v1", tags=["voto"])


# Alias para el servicio de voto
get_voto_service = Depends(IVotoService)


@voto_router.post("/voto", status_code=status.HTTP_201_CREATED)
async def create_voto(voto: VotoDTOCreate, 
                      voto_service: IVotoService = Depends(build_voto_service)
                      ):
    """
    Crear un nuevo voto.
    """
    try:
        await voto_service.create_service(map_dto_voto(voto))
        return {"message": "Voto creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear voto: {str(e)}")

@voto_router.get("/voto", status_code=status.HTTP_200_OK)
async def get_voto(
    voto_service: IVotoService = Depends(build_voto_service)
):
    """
    Obtener todos los votos.
    """
    try:
        return await voto_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener votos: {str(e)}")

@voto_router.put("/voto/{id}", status_code=status.HTTP_200_OK)
async def update_voto(id: int, voto: VotoDTOUpdate, voto_service: IVotoService = Depends(build_voto_service)):
    """
    Actualizar un voto existente.
    """
    try:
        voto_domain = map_dto_voto(voto)
        voto_domain.id = id  # Asignar ID al dominio del voto
        await voto_service.update_service(voto_domain)
        return {"message": "Voto actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar voto: {str(e)}")

@voto_router.delete("/voto/{id}", status_code=status.HTTP_200_OK)
async def delete_voto(id: int, voto_service: IVotoService = Depends(build_voto_service)):
    """
    Eliminar un voto por ID.
    """
    try:
        await voto_service.delete_service(id)
        return {"message": "Voto eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar voto: {str(e)}")
    

