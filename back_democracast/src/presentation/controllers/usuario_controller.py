from fastapi import APIRouter, Depends, HTTPException, status

from src.core.abstractions.services.usuario_service_abstract import IUsuarioService
from src.core.dependency_inyection.dependency_inyection import build_usuario_service
from src.presentation.dto.usuario_dto import UsuarioDTOLogin, UsuarioDTOCreate
from src.presentation.mappers.map_dto_domain_usuario import map_dto_usuario
from src.utils.auth import generar_token

usuario_router = APIRouter(prefix="/api/v1", tags=["usuario"])

# Alias para el servicio de usuario
get_usuario_service = Depends(IUsuarioService)


@usuario_router.post("/usuario", status_code=status.HTTP_201_CREATED)
async def create_usuario(usuario: UsuarioDTOCreate, 
                         usuario_service: IUsuarioService = Depends(build_usuario_service)
                         ):
    """
    Crear un nuevo usuario.
    """
    try:
        await usuario_service.create_service(map_dto_usuario(usuario))
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear usuario: {str(e)}")


@usuario_router.get("/usuario", status_code=status.HTTP_200_OK)
async def get_usuario(
    usuario_service: IUsuarioService = Depends(build_usuario_service)
):
    """
    Obtener todos los usuarios.
    """
    try:
        return await usuario_service.get_all_service()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al obtener usuarios: {str(e)}")


@usuario_router.put("/usuario/{id}", status_code=status.HTTP_200_OK)
async def update_usuario(id: int, usuario: UsuarioDTOCreate, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    """
    Actualizar un usuario existente.
    """
    try:
        usuario_domain = map_dto_usuario(usuario)
        usuario_domain.id = id  # Asignar ID al dominio del usuario
        await usuario_service.update_service(usuario_domain)
        return {"message": "Usuario actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar usuario: {str(e)}")


@usuario_router.delete("/usuario/{id}", status_code=status.HTTP_200_OK)
async def delete_usuario(id: int, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    """
    Eliminar un usuario por ID.
    """
    try:
        await usuario_service.delete_service(id)
        return {"message": "Usuario eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al eliminar usuario: {str(e)}")


@usuario_router.post("/usuario/login", status_code=status.HTTP_200_OK)
async def login(usuario: UsuarioDTOLogin, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    """
    Inicio de sesión para usuarios.
    """
    try:
        user = await usuario_service.login_service(usuario.usuario, usuario.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
        token = generar_token(user.id, user.usuario, user.rol_id)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al iniciar sesión: {str(e)}")


@usuario_router.post("/usuario/logout", status_code=status.HTTP_200_OK)
async def logout(id: int, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    """
    Cerrar sesión para usuarios.
    """
    try:
        await usuario_service.logout_service(id)
        return {"message": "Usuario deslogueado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al cerrar sesión: {str(e)}")
