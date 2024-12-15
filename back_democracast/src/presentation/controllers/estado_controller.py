from fastapi import APIRouter, Depends, HTTPException, status

from src.core.abstractions.services.estado_service_abstract import IEstadoService
from src.core.dependency_inyection.dependency_inyection import build_estado_service
from src.presentation.dto.estado_dto import EstadoDTOCreate
from src.presentation.mappers.map_dto_domain_estado import map_dto_estado

estado_router = APIRouter(prefix="/api/v1", tags=["estado"])


# Alias para el servicio de estado
get_estado_service = Depends(IEstadoService)


@estado_router.post("/estado", status_code=status.HTTP_201_CREATED)
async def create_estado(estado: EstadoDTOCreate, 
                        estado_service: IEstadoService = Depends(build_estado_service)
                        ):
    """
    Crear un nuevo estado.
    """
    try:
        await estado_service.create_service(map_dto_estado(estado))
        return {"message": "Estado creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear estado: {str(e)}")


@estado_router.get("/estado", status_code=status.HTTP_200_OK)
async def get_estado(
    estado_service: IEstadoService = Depends(build_estado_service)
):
    """
    Obtener todos los estados.
    """
    try:
        return await estado_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener estados: {str(e)}")


@estado_router.put("/estado/{id}", status_code=status.HTTP_200_OK)
async def update_estado(id: int, estado: EstadoDTOCreate, estado_service: IEstadoService = Depends(build_estado_service)):
    """
    Actualizar un estado existente.
    """
    try:
        estado_domain = map_dto_estado(estado)
        estado_domain.id = id  # Asignar ID al dominio del estado
        await estado_service.update_service(estado_domain)
        return {"message": "Estado actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar estado: {str(e)}")

@estado_router.delete("/estado/{id}", status_code=status.HTTP_200_OK)
async def delete_estado(id: int, estado_service: IEstadoService = Depends(build_estado_service)):
    """
    Eliminar un estado por ID.
    """
    try:
        await estado_service.delete_service(id)
        return {"message": "Estado eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar estado: {str(e)}")


