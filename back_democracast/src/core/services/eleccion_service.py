from src.core.abstractions.infraestructure.respository.eleccion_repository_abstract import IEleccionRepository, EleccionDomain
from src.core.abstractions.services.eleccion_service_abstract import IEleccionService

class EleccionService(IEleccionService):
    
    def __init__(self, eleccion_repository: IEleccionRepository):
        self.eleccion_repository = eleccion_repository
    
    async def get_all_service(self) -> list[EleccionDomain]:
        return await self.eleccion_repository.get_all()
    
    async def get_by_name_service(self, name: str) -> EleccionDomain:
        return await self.eleccion_repository.get_by_name(name)
    
    async def get_by_id_service(self, id: int) -> EleccionDomain:
        return await self.eleccion_repository.get_by_id(id)
    
    async def create_service(self, eleccion: EleccionDomain):
        print("IN sSERVER")
        return await self.eleccion_repository.create(eleccion)
    
    async def update_service(self, eleccion: EleccionDomain):
        return await self.eleccion_repository.update(eleccion)
    
    
    async def delete_service(self, id: int):
        return await self.eleccion_repository.delete(id)
    
    
    