from src.core.abstractions.infraestructure.respository.rol_repository_abstract import IRolRepository, RolDomain 
from src.core.abstractions.services.rol_service_abstract import IRolService

class RolService(IRolService):
        
        def __init__(self, rol_repository: IRolRepository):
            self.rol_repository = rol_repository
        
        async def get_all_service(self) -> list[RolDomain]:
            return await self.rol_repository.get_all()
        
        async def get_by_id_service(self, id: int) -> RolDomain:
            return await self.rol_repository.get_by_id(id)
        
        async def create_service(self, rol: RolDomain):
            return await self.rol_repository.create(rol)
        
        async def update_service(self, rol: RolDomain):
            return await self.rol_repository.update(rol)
        
        async def delete_service(self, id: int):
            return await self.rol_repository.delete(id)