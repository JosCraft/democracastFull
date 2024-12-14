from abc import abstractmethod
from src.core.models.persona_domain import PersonaDomain

class IPersonaService:

    @abstractmethod
    async def get_all_service(self) -> list[PersonaDomain]:
        pass

    @abstractmethod
    async def get_by_id_service(self, id: int) -> PersonaDomain:
        pass
    @abstractmethod
    async def get_by_name_service(self, name: str) -> PersonaDomain:
        pass
    
    @abstractmethod
    async def create_service(self, persona: PersonaDomain):
        pass
    @abstractmethod
    async def update_service(self, persona: PersonaDomain):
        pass
    @abstractmethod
    async def delete_service(self, id: int):
        pass