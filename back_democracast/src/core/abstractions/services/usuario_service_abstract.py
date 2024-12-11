from abc import abstractmethod
from src.core.models.usuario_domain import UsuarioDomain

class IUsuarioService:
    
    @abstractmethod
    async def get_all_service(self) -> list[UsuarioDomain]: 
        pass

    @abstractmethod
    async def create_service(self, usuario: UsuarioDomain):
        pass

    @abstractmethod
    async def update_service(self, usuario: UsuarioDomain):
        pass

    @abstractmethod
    async def delete_service(self, id: int):
        pass
    
    @abstractmethod
    async def login_service(self, usuario: str, password: str) -> UsuarioDomain:
        pass
    
    @abstractmethod
    async def logout_service(self, id: int):
        pass
    