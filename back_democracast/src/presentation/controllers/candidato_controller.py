from fastapi import APIRouter, Depends, HTTPException,status

from src.core.abstractions.services.candidato_service_abstract import ICandidatoService
from src.core.dependency_inyection.dependency_inyection import build_candidato_service
from src.presentation.dto.candidato_dto import CandidatoDTOCreate, CandidatoDTOUpdate
from src.presentation.mappers.map_dto_domain_candidato import map_dto_candidato

candidato_router = APIRouter(prefix="/api/v1", tags=["candidato"])

# Alias para el servicio de candidato
get_candidato_service = Depends(ICandidatoService)


@candidato_router.post("/candidato", status_code=status.HTTP_201_CREATED)
async def create_candidato(candidato: CandidatoDTOCreate, 
                           candidato_service: ICandidatoService = Depends(build_candidato_service)
                           ):
    """
    Crear un nuevo candidato.
    """
    try:
        await candidato_service.create_service(map_dto_candidato(candidato))
        return {"message": "Candidato creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear candidato: {str(e)}")

@candidato_router.get("/candidato", status_code=status.HTTP_200_OK)
async def get_candidato(
    candidato_service: ICandidatoService = Depends(build_candidato_service)
):
    """
    Obtener todos los candidatos.
    """
    try:
        return await candidato_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener candidatos: {str(e)}")

@candidato_router.put("/candidato/{id}", status_code=status.HTTP_200_OK)
async def update_candidato(id: int, candidato: CandidatoDTOUpdate, candidato_service: ICandidatoService = Depends(build_candidato_service)):
    """
    Actualizar un candidato existente.
    """
    try:
        candidato_domain = map_dto_candidato(candidato)
        candidato_domain.id = id  # Asignar ID al dominio del candidato
        await candidato_service.update_service(candidato_domain)
        return {"message": "Candidato actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar candidato: {str(e)}")

@candidato_router.delete("/candidato/{id}", status_code=status.HTTP_200_OK)
async def delete_candidato(id: int, candidato_service: ICandidatoService = Depends(build_candidato_service)):
    """
    Eliminar un candidato por ID.
    """
    try:
        await candidato_service.delete_service(id)
        return {"message": "Candidato eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar candidato: {str(e)}")

@candidato_router.get("/candidato/{id}", status_code=status.HTTP_200_OK)
async def get_candidato_by_id(id: int, candidato_service: ICandidatoService = Depends(build_candidato_service)):
    """
    Obtener un candidato por ID.
    """
    try:
        return await candidato_service.get_by_id_service(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener candidato por ID: {str(e)}")





