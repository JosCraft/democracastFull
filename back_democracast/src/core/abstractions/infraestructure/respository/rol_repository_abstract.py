from abc import abstractmethod
from src.core.models.rol_domain import RolDomain

class IRolRepository:
    
    @abstractmethod
    async def get_all(self) -> list[RolDomain]:
        pass
    @abstractmethod
    async def get_by_id(self, id: int) -> RolDomain:
        pass
    
    @abstractmethod
    async def create(self, rol: RolDomain):
        pass

    @abstractmethod
    async def update(self, rol: RolDomain):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass
    
   