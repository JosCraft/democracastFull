from abc import abstractmethod
from src.core.models.rol_domain import RolDomain

class IRolService:
    @abstractmethod
    async def get_all_service(self) -> list[RolDomain]:
        pass
    @abstractmethod
    async def get_by_id_service(self, id: int) -> RolDomain:
        pass
    
    @abstractmethod
    async def create_service(self, rol: RolDomain):
        pass
    @abstractmethod
    async def update_service(self, rol: RolDomain):
        pass
    @abstractmethod
    async def delete_service(self, id: int):
        pass