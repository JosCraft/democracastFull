from src.core.abstractions.infraestructure.respository.estado_repository_abstract import IEstadoRepository, EstadoDomain    
from src.core.abstractions.services.estado_service_abstract import IEstadoService

class EstadoService(IEstadoService):
        
        def __init__(self, estado_repository: IEstadoRepository):
            self.estado_repository = estado_repository
        
        async def get_all_service(self) -> list[EstadoDomain]:
            return await self.estado_repository.get_all()
        
        async def create_service(self, estado: EstadoDomain):
            print("IN sSERVER")
            return await self.estado_repository.create(estado)
        
        async def update_service(self, estado: EstadoDomain):
            return await self.estado_repository.update(estado)
        
        async def delete_service(self, id: int):
            return await self.estado_repository.delete(id)
        
        async def get_by_id_service(self, id: int) -> EstadoDomain:
            return await self.estado_repository.get_by_id(id)
        
        async def get_by_name_service(self, name: str) -> EstadoDomain:
            return await self.estado_repository.get_by_name(name)
        
        