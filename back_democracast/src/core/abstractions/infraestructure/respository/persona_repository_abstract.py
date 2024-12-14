from abc import abstractmethod
from src.core.models.persona_domain import PersonaDomain

class IPersonaRepository:
    
    @abstractmethod
    async def get_all(self) -> list[PersonaDomain]:
        pass
    
    @abstractmethod
    async def get_by_id(self, id: int) -> PersonaDomain:
        pass
    @abstractmethod
    async def get_by_name(self, name: str) -> PersonaDomain:
        pass
    @abstractmethod
    async def create(self, persona: PersonaDomain):
        pass

    @abstractmethod
    async def update(self, persona: PersonaDomain):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass
    
   