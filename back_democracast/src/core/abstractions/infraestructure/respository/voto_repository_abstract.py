from abc import abstractmethod
from src.core.models.voto_domain import VotoDomain

class IVotoRepository:
        
        @abstractmethod
        async def get_all(self) -> list[VotoDomain]:
            pass
        @abstractmethod
        async def get_by_id(self, id: int) -> VotoDomain:
            pass
        
        @abstractmethod
        async def create(self, voto: VotoDomain):
            pass
    
        @abstractmethod
        async def update(self, voto: VotoDomain):
            pass
    
        @abstractmethod
        async def delete(self, id: int):
            pass