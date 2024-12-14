from abc import abstractmethod
from src.core.models.voto_domain import VotoDomain
class IVotoService:
    
    @abstractmethod
    async def get_all_service(self) -> list[VotoDomain]:
        pass
    @abstractmethod
    async def get_by_id_service(self, id: int) -> VotoDomain:
        pass
    
    @abstractmethod
    async def create_service(self, voto: VotoDomain):
        pass
    
    @abstractmethod
    async def update_service(self, voto: VotoDomain):
        pass
    
    @abstractmethod
    async def delete_service(self, id: int):
        pass