from src.core.abstractions.infraestructure.respository.rol_repository_abstract import IRolRepository
from src.core.models.rol_domain import RolDomain

class RolRepository(IRolRepository):

    def __init__(self, connection):
        self.connection = connection
    
    async def get_all(self) -> list[RolDomain]:
        query = "SELECT id, nombre FROM rol"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    RolDomain(
                        id=row['id'],
                        nombre=row['nombre']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all roles: {e}")
    
    async def create(self, rol: RolDomain) -> None:
        query = "INSERT INTO rol (nombre) VALUES (%s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (rol.nombre,))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating role: {e}")
    
    async def update(self, rol: RolDomain) -> None:
        query = "UPDATE rol SET nombre=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (rol.nombre, rol.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating role: {e}")
    
    async def delete(self, id: int) -> None:
        query = "DELETE FROM rol WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting role: {e}")
