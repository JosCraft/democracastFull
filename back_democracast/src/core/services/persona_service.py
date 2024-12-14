from src.core.abstractions.infraestructure.respository.persona_repository_abstract import IPersonaRepository, PersonaDomain 
from src.core.abstractions.services.persona_service_abstract import IPersonaService

class PersonaService(IPersonaService):
        
        def __init__(self, persona_repository: IPersonaRepository):
            self.persona_repository = persona_repository
        
        async def get_all_service(self) -> list[PersonaDomain]:
            return await self.persona_repository.get_all()
        
        async def create_service(self, persona: PersonaDomain):
            print("IN sSERVER")
            return await self.persona_repository.create(persona)
        
        async def update_service(self, persona: PersonaDomain):
            return await self.persona_repository.update(persona)
        
        async def delete_service(self, id: int):
            return await self.persona_repository.delete(id)
        
        async def get_by_id_service(self, id: int) -> PersonaDomain:
            return await self.persona_repository.get_by_id(id)
        
        async def get_by_name_service(self, name: str) -> PersonaDomain:
            return await self.persona_repository.get_by_name(name)