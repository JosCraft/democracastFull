from src.core.abstractions.infraestructure.respository.voto_repository_abstract import IVotoRepository, VotoDomain  
from src.core.abstractions.services.voto_service_abstract import IVotoService

class VotoService(IVotoService):
        
        def __init__(self, voto_repository: IVotoRepository):
            self.voto_repository = voto_repository
        
        async def get_all_service(self) -> list[VotoDomain]:
            return await self.voto_repository.get_all()
        
        async def get_by_id_service(self, id: int) -> VotoDomain:
            return await self.voto_repository.get_by_id(id)
        
        async def create_service(self, voto: VotoDomain):
            return await self.voto_repository.create(voto)
        
        async def update_service(self, voto: VotoDomain):
            return await self.voto_repository.update(voto)
        
        async def delete_service(self, id: int):
            return await self.voto_repository.delete(id)
        