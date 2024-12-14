from abc import abstractmethod
from src.core.models.estado_domain import EstadoDomain

class IEstadoRepository:
    
    @abstractmethod
    async def get_all(self) -> list[EstadoDomain]:
        pass
    
    @abstractmethod
    async def create(self, estado: EstadoDomain):
        pass

    @abstractmethod
    async def update(self, estado: EstadoDomain):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass