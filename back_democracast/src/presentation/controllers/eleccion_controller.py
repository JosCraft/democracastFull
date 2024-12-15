from fastapi import APIRouter, Depends, HTTPException, status

from src.core.abstractions.services.eleccion_service_abstract import IEleccionService
from src.core.dependency_inyection.dependency_inyection import build_eleccion_service
from src.presentation.dto.eleccion_dto import EleccionDTOCreate
from src.presentation.mappers.map_dto_domain_eleccion import map_dto_eleccion

eleccion_router = APIRouter(prefix="/api/v1", tags=["eleccion"])

# Alias para el servicio de eleccion
get_eleccion_service = Depends(IEleccionService)


@eleccion_router.post("/eleccion", status_code=status.HTTP_201_CREATED)
async def create_eleccion(eleccion: EleccionDTOCreate, 
                         eleccion_service: IEleccionService = Depends(build_eleccion_service)
                         ):
    """
    Crear una nueva eleccion.
    """
    try:
        await eleccion_service.create_service(map_dto_eleccion(eleccion))
        return {"message": "Eleccion creada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear eleccion: {str(e)}")

@eleccion_router.get("/eleccion", status_code=status.HTTP_200_OK)
async def get_eleccion(
    eleccion_service: IEleccionService = Depends(build_eleccion_service)
):
    """
    Obtener todas las elecciones.
    """
    try:
        return await eleccion_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener elecciones: {str(e)}")   
 
@eleccion_router.put("/eleccion/{id}", status_code=status.HTTP_200_OK)
async def update_eleccion(id: int, eleccion: EleccionDTOCreate, eleccion_service: IEleccionService = Depends(build_eleccion_service)):
    """
    Actualizar una eleccion existente.
    """
    try:
        eleccion_domain = map_dto_eleccion(eleccion)
        eleccion_domain.id = id  # Asignar ID al dominio de la eleccion
        await eleccion_service.update_service(eleccion_domain)
        return {"message": "Eleccion actualizada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar eleccion: {str(e)}")

@eleccion_router.delete("/eleccion/{id}", status_code=status.HTTP_200_OK)
async def delete_eleccion(id: int, eleccion_service: IEleccionService = Depends(build_eleccion_service)):
    """
    Eliminar una eleccion por ID.
    """
    try:
        await eleccion_service.delete_service(id)
        return {"message": "Eleccion eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar eleccion: {str(e)}")

@eleccion_router.get("/eleccion/{id}", status_code=status.HTTP_200_OK)
async def get_eleccion_by_id(id: int, eleccion_service: IEleccionService = Depends(build_eleccion_service)):
    """
    Obtener una eleccion por ID.
    """
    try:
        return await eleccion_service.get_by_id_service(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener eleccion por ID: {str(e)}")
                           

