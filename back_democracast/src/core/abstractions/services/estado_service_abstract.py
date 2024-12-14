from abc import abstractmethod 
from src.core.models.estado_domain import EstadoDomain
 
class IEstadoService:
    
    @abstractmethod
    async def get_all_service(self) -> list[EstadoDomain]:
        pass

    @abstractmethod
    async def create_service(self, estado: EstadoDomain):
        pass

    @abstractmethod
    async def update_service(self, estado: EstadoDomain):
        pass

    @abstractmethod
    async def delete_service(self, id: int):
        pass