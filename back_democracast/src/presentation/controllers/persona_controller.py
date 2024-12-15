from fastapi import APIRouter, Depends, HTTPException, status

from src.core.abstractions.services.persona_service_abstract import IPersonaService
from src.core.dependency_inyection.dependency_inyection import build_persona_service
from src.presentation.dto.persona_dto import PersonaDTOCreate
from src.presentation.mappers.map_dto_domain_persona import map_dto_persona

persona_router = APIRouter(prefix="/api/v1", tags=["persona"])

# Alias para el servicio de persona
get_persona_service = Depends(IPersonaService)


@persona_router.post("/persona", status_code=status.HTTP_201_CREATED)
async def create_persona(persona: PersonaDTOCreate, 
                         persona_service: IPersonaService = Depends(build_persona_service)
                         ):
    """
    Crear una nueva persona.
    """
    try:
        await persona_service.create_service(map_dto_persona(persona))
        return {"message": "Persona creada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear persona: {str(e)}  ") 
    

@persona_router.get("/persona", status_code=status.HTTP_200_OK)
async def get_persona(
    persona_service: IPersonaService = Depends(build_persona_service)
):
    """
    Obtener todas las personas.
    """
    try:
        return await persona_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener personas: {str(e)}")
                             
@persona_router.put("/persona/{id}", status_code=status.HTTP_200_OK)
async def update_persona(id: int, persona: PersonaDTOCreate, persona_service: IPersonaService = Depends(build_persona_service)):
    """
    Actualizar una persona existente.
    """
    try:
        persona_domain = map_dto_persona(persona)
        persona_domain.id = id  # Asignar ID al dominio de la persona
        await persona_service.update_service(persona_domain)
        return {"message": "Persona actualizada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar persona: {str(e)}")

@persona_router.delete("/persona/{id}", status_code=status.HTTP_200_OK)
async def delete_persona(id: int, persona_service: IPersonaService = Depends(build_persona_service)):
    """
    Eliminar una persona por ID.
    """
    try:
        await persona_service.delete_service(id)
        return {"message": "Persona eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar persona: {str(e)}")

@persona_router.get("/persona/{id}", status_code=status.HTTP_200_OK)
async def get_persona_by_id(id: int, persona_service: IPersonaService = Depends(build_persona_service)):
    """
    Obtener una persona por ID.
    """
    try:
        return await persona_service.get_by_id_service(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener persona: {str(e)}")


@persona_router.get("/persona/nombre/{nombre}", status_code=status.HTTP_200_OK)
async def get_persona_by_nombre(nombre: str, persona_service: IPersonaService = Depends(build_persona_service)):
    """
    Obtener una persona por nombre.
    """
    try:
        return await persona_service.get_by_nombre_service(nombre)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener persona: {str(e)}")


@persona_router.get("/persona/apellido/{apellido}", status_code=status.HTTP_200_OK)
async def get_persona_by_apellido(apellido: str, persona_service: IPersonaService = Depends(build_persona_service)):
    """
    Obtener una persona por apellido.
    """
    try:
        return await persona_service.get_by_apellido_service(apellido)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener persona: {str(e)}")

