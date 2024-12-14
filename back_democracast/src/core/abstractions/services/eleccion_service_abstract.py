from abc import abstractmethod
from src.core.models.eleccion_domain import EleccionDomain

class IEleccionService:
    
    @abstractmethod
    async def get_all_service(self) -> list[EleccionDomain]: 
        pass
    @abstractmethod
    async def get_by_id_service(self, id: int) -> EleccionDomain:
        pass
    @abstractmethod
    async def get_by_name_service(self, name: str) -> EleccionDomain:
        pass
    
    @abstractmethod
    async def create_service(self, eleccion: EleccionDomain):
        pass
    @abstractmethod
    async def update_service(self, eleccion: EleccionDomain):
        pass    
    @abstractmethod
    async def delete_service(self, id: int):
        pass