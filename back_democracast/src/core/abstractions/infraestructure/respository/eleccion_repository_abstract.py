from abc import abstractmethod
from src.core.models.eleccion_domain import EleccionDomain

class IEleccionRepository:
        
        @abstractmethod
        async def get_all(self) -> list[EleccionDomain]:
            pass
        @abstractmethod
        async def get_by_name(self, name: str) -> EleccionDomain:
            pass
        
        @abstractmethod
        async def get_by_id(self, id: int) -> EleccionDomain:
            pass
        
        @abstractmethod
        async def create(self, eleccion: EleccionDomain):
            pass
    
        @abstractmethod
        async def update(self, eleccion: EleccionDomain):
            pass
    
        @abstractmethod
        async def delete(self, id: int):
            pass
        