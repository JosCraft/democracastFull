from src.core.abstractions.infraestructure.respository.candidato_repository_abstract import ICandidatoRepository, CandidatoDomain
from src.core.abstractions.services.candidato_service_abstract import ICandidatoService

class CandidatoService(ICandidatoService):
    
    def __init__(self, candidato_repository: ICandidatoRepository):
        self.candidato_repository = candidato_repository
    
    async def get_all_service(self) -> list[CandidatoDomain]:
        return await self.candidato_repository.get_all()
    
    async def get_by_id_service(self, id: int) -> CandidatoDomain:
        return await self.candidato_repository.get_by_id(id)
    
    async def get_by_name_service(self, name: str) -> CandidatoDomain:
        return await self.candidato_repository.get_by_name(name)
    
    async def create_service(self, candidato: CandidatoDomain):
        print("IN sSERVER")
        return await self.candidato_repository.create(candidato)
    
    async def update_service(self, candidato: CandidatoDomain):
        return await self.candidato_repository.update(candidato)
    
    async def delete_service(self, id: int):
        return await self.candidato_repository.delete(id)
    
    