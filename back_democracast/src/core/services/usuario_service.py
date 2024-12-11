from src.core.abstractions.infraestructure.respository.usuario_repository_abstract import IUsuarioRepository, UsuarioDomain
from src.core.abstractions.services.usuario_service_abstract import IUsuarioService

class UsuarioService(IUsuarioService):
    
    def __init__(self, usuario_repository: IUsuarioRepository):
        self.usuario_repository = usuario_repository
    
    async def get_all_service(self) -> list[UsuarioDomain]:
        return await self.usuario_repository.get_all()
    
    async def create_service(self, usuario: UsuarioDomain):
        print("IN sSERVER")
        return await self.usuario_repository.create(usuario)
    
    async def update_service(self, usuario: UsuarioDomain):
        return await self.usuario_repository.update(usuario)
    
    async def delete_service(self, id: int):
        return await self.usuario_repository.delete(id)
    
    async def login_service(self, usuario: str, password: str) -> UsuarioDomain:
        return await self.usuario_repository.login(usuario, password)
    
    async def logout_service(self, id: int):
        return await self.usuario_repository.logout(id)
    