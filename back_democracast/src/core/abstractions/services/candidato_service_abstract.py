from abc import abstractmethod
from src.core.models.candidato_domain import CandidatoDomain

class ICandidatoService:
    
    @abstractmethod
    async def get_all_service(self) -> list[CandidatoDomain]: 
        pass
    @abstractmethod
    async def get_by_id_service(self, id: int) -> CandidatoDomain:
        pass
    
    @abstractmethod
    async def create_service(self, candidato: CandidatoDomain):
        pass

    @abstractmethod
    async def update_service(self, candidato: CandidatoDomain):
        pass

    @abstractmethod 
    async def delete_service(self, id: int):
        pass

    
