from abc import abstractmethod
from src.core.models.usuario_domain import UsuarioDomain


class IUsuarioRepository:
    
    @abstractmethod
    async def get_all(self) -> list[UsuarioDomain]:
        pass

    @abstractmethod
    async def create(self, usuario: UsuarioDomain):
        pass

    @abstractmethod
    async def update(self, usuario: UsuarioDomain):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass
    
    @abstractmethod
    async def login(self, usuario: str, password: str) -> UsuarioDomain:
        pass
    
    @abstractmethod
    async def logout(self, id: int):
        pass
    
    
