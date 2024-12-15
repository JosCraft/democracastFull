from src.core.abstractions.infraestructure.respository.persona_repository_abstract import IPersonaRepository
from src.core.models.persona_domain import PersonaDomain

class PersonaRepository(IPersonaRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[PersonaDomain]:
        query = "SELECT id, nombre, apellido FROM persona"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    PersonaDomain(
                        id=row['id'], 
                        nombre=row['nombre'], 
                        apellido=row['apellido'], 
                       
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all people: {e}")
            return []

    async def create(self, persona: PersonaDomain) -> None:
        query = "INSERT INTO persona (nombre, apellido) VALUES (%s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (persona.nombre, persona.apellido))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating person: {e}")
    
    async def update(self, persona: PersonaDomain) -> None:
        query = "UPDATE persona SET nombre=%s, apellido=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (persona.nombre, persona.apellido, persona.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating person: {e}")
    
    async def delete(self, id: int) -> None:
        query = "DELETE FROM persona WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting person: {e}")
    
    async def get_by_id(self, id: int) -> PersonaDomain:
        query = "SELECT id, nombre, apellido FROM persona WHERE id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                return PersonaDomain(
                    id=result['id'],
                    nombre=result['nombre'],
                    apellido=result['apellido']
                )
        except Exception as e:
            print(f"Error fetching person by id: {e}")
            return PersonaDomain(
                id=0,
                nombre="",
                apellido=""
            )
    
    async def get_by_name(self, nombre: str) -> PersonaDomain:
        query = "SELECT id, nombre, apellido FROM persona WHERE nombre=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (nombre,))
                result = cursor.fetchone()
                return PersonaDomain(
                    id=result['id'],
                    nombre=result['nombre'],
                    apellido=result['apellido']
                )
        except Exception as e:
            print(f"Error fetching person by name: {e}")
            return PersonaDomain(
                id=0,
                nombre="",
                apellido=""
            )
    async def get_by_apellido(self, apellido: str) -> PersonaDomain:
        query = "SELECT id, nombre, apellido FROM persona WHERE apellido=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (apellido,))
                result = cursor.fetchone()
                return PersonaDomain(
                    id=result['id'],
                    nombre=result['nombre'],
                    apellido=result['apellido']
                )
        except Exception as e:
            print(f"Error fetching person by apellido: {e}")
            return PersonaDomain(
                id=0,
                nombre="",
                apellido=""
            )
        

        
