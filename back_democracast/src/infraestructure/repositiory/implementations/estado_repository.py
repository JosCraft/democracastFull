from src.core.abstractions.infraestructure.respository.estado_repository_abstract import IEstadoRepository
from src.core.models.estado_domain import EstadoDomain

class EstadoRepository(IEstadoRepository):

    def __init__(self, connection):
        self.connection = connection
    
    async def get_all(self) -> list[EstadoDomain]:
        query = "SELECT id, nombre FROM estado"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    EstadoDomain(
                        id=row['id'],
                        nombre=row['nombre']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all states: {e}")

    async def create(self, estado: EstadoDomain) -> None:
        query = "INSERT INTO estado (nombre) VALUES (%s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (estado.nombre,))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating state: {e}")
    
    async def update(self, estado: EstadoDomain) -> None:
        query = "UPDATE estado SET nombre=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (estado.nombre, estado.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating state: {e}")
    
    async def delete(self, id: int) -> None:
        query = "DELETE FROM estado WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting state: {e}")
            


