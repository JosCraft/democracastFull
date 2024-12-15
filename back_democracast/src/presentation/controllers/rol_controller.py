from fastapi import APIRouter, Depends, HTTPException, status

from src.core.abstractions.services.rol_service_abstract import IRolService
from src.core.dependency_inyection.dependency_inyection import build_rol_service
from src.presentation.dto.rol_dto import RolDTOCreate
from src.presentation.mappers.map_dto_domain_rol import map_dto_rol


rol_router = APIRouter(prefix="/api/v1", tags=["rol"])


# Alias para el servicio de rol
get_rol_service = Depends(IRolService)

@rol_router.post("/rol", status_code=status.HTTP_201_CREATED)
async def create_rol(rol: RolDTOCreate, 
                     rol_service: IRolService = Depends(build_rol_service)
                     ):
    """
    Crear un nuevo rol.
    """
    try:
        await rol_service.create_service(map_dto_rol(rol))
        return {"message": "Rol creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear rol: {str(e)}")
    
@rol_router.get("/rol", status_code=status.HTTP_200_OK)
async def get_rol(
    rol_service: IRolService = Depends(build_rol_service)
):
    """
    Obtener todos los roles.
    """
    try:
        return await rol_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener roles: {str(e)}")
    
@rol_router.put("/rol/{id}", status_code=status.HTTP_200_OK)
async def update_rol(id: int, rol: RolDTOCreate, rol_service: IRolService = Depends(build_rol_service)):
    """
    Actualizar un rol existente.
    """
    try:
        rol_domain = map_dto_rol(rol)
        rol_domain.id = id  # Asignar ID al dominio del rol
        await rol_service.update_service(rol_domain)
        return {"message": "Rol actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar rol: {str(e)}")


@rol_router.delete("/rol/{id}", status_code=status.HTTP_200_OK)
async def delete_rol(id: int, rol_service: IRolService = Depends(build_rol_service)):
    """
    Eliminar un rol por ID.
    """
    try:
        await rol_service.delete_service(id)
        return {"message": "Rol eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar rol: {str(e)}")
