from fastapi import FastAPI
from fastapi import Depends
from src.core.services.usuario_service import UsuarioService

from src.infraestructure.repositiory.dependency_inyection.dependency_inyection import get_db_connection

from src.infraestructure.repositiory.implementations.usuario_repository import UsuarioRepository


def build_usuario_service(
    db_connection=Depends(get_db_connection)
):
    return UsuarioService(UsuarioRepository(db_connection))
