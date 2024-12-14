from abc import abstractmethod
from src.core.models.candidato_domain import CandidatoDomain

class ICandidatoRepository:
    
    @abstractmethod
    async def get_all(self) -> list[CandidatoDomain]:
        pass
    @abstractmethod
    async def get_by_name(self, name: str) -> CandidatoDomain:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> CandidatoDomain:
        pass

    @abstractmethod
    async def create(self, candidato: CandidatoDomain):
        pass

    @abstractmethod
    async def update(self, candidato: CandidatoDomain):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass