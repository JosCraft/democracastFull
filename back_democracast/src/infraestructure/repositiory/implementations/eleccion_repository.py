from datetime import date
from src.core.abstractions.infraestructure.respository.usuario_repository_abstract import IEleccionRepository
from src.core.models.eleccion_domain import EleccionDomain

class EleccionRepository(IEleccionRepository):

    def __init__(self, connection):
        self.connection = connection
    
    async def get_all(self) -> list[EleccionDomain]:
        query = "SELECT id, nombre, fecha, estado_id, votospermitidos FROM eleccion"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    EleccionDomain(
                        id=row['id'],
                        nombre=row['nombre'],
                        fecha=row['fecha'],
                        estado_id=row['estado_id'],
                        votospermitidos=row['votospermitidos']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all elections: {e}")    

    
    async def create(self, eleccion: EleccionDomain) -> None:
        query = "INSERT INTO eleccion (nombre, fecha, estado_id,votospermitidos) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (eleccion.nombre, eleccion.fecha, eleccion.estado_id, eleccion.votospermitidos))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating election: {e}")

    async def update(self, eleccion: EleccionDomain) -> None:
        query = "UPDATE eleccion SET nombre=%s, fecha=%s, estado_id=%s, votospermitidos=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (eleccion.nombre, eleccion.fecha, eleccion.estado_id, eleccion.votospermitidos, eleccion.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating election: {e}")

    async def delete(self, id: int) -> None:
        query = "DELETE FROM eleccion WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting election: {e}")

    async def get_by_id(self, id: int) -> EleccionDomain:
        query = "SELECT id, nombre, fecha, estado_id, votospermitidos FROM eleccion WHERE id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                return EleccionDomain(
                    id=result['id'],
                    nombre=result['nombre'],
                    fecha=result['fecha'],
                    estado_id=result['estado_id'],
                    votospermitidos=result['votospermitidos']
                )
        except Exception as e:
            print(f"Error fetching election by id: {e}")
            return None
    
    async def get_by_name(self, nombre: str) -> EleccionDomain:
        query = "SELECT id, nombre, fecha, estado_id, votospermitidos FROM eleccion WHERE nombre=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (nombre,))
                result = cursor.fetchone()
                return EleccionDomain(
                    id=result['id'],
                    nombre=result['nombre'],
                    fecha=result['fecha'],
                    estado_id=result['estado_id'],
                    votospermitidos=result['votospermitidos']
                )
        except Exception as e:
            print(f"Error fetching election by name: {e}")
            return None
    
    async def get_by_estado_id(self, estado_id: int) -> list[EleccionDomain]:
        query = "SELECT id, nombre, fecha, estado_id, votospermitidos FROM eleccion WHERE estado_id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (estado_id,))
                result = cursor.fetchall()
                return [
                    EleccionDomain(
                        id=row['id'],
                        nombre=row['nombre'],
                        fecha=row['fecha'],
                        estado_id=row['estado_id'],
                        votospermitidos=row['votospermitidos']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching elections by estado ID: {e}")
            return []
    
    async def get_by_fecha(self, fecha: date) -> list[EleccionDomain]:
        query = "SELECT id, nombre, fecha, estado_id, votospermitidos FROM eleccion WHERE fecha=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (fecha,))
                result = cursor.fetchall()
                return [
                    EleccionDomain(
                        id=row['id'],
                        nombre=row['nombre'],
                        fecha=row['fecha'],
                        estado_id=row['estado_id'],
                        votospermitidos=row['votospermitidos']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching elections by fecha: {e}")
            return []
    
    

    
