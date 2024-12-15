from src.core.abstractions.infraestructure.respository.candidato_repository_abstract import ICandidatoRepository
from src.core.models.candidato_domain import CandidatoDomain


class CandidatoRepository(ICandidatoRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[CandidatoDomain]:
        query = "SELECT id, nombre, apellido, partido_id, estado_id FROM candidato"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    CandidatoDomain(
                        id=row['id'],
                        numero_cartelera=row['numero_cartelera'],
                        cantidad_votos=row['cantidad_votos'],
                        eleccion_id=row['eleccion_id'],
                        persona_id=row['persona_id']

                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all candidates: {e}")
            return []
    
    async def create(self, candidato: CandidatoDomain) -> None:
        query = "INSERT INTO candidato (numero_cartelera,cantidad_votos,eleccion_id,persona_id) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (candidato.nombre, candidato.apellido, candidato.partido_id, 1))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating candidate: {e}")

    async def update(self, candidato: CandidatoDomain) -> None:
        query = "UPDATE candidato SET numero_cartelera=%s, cantidad_votos=%s, eleccion_id=%s, persona_id=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (candidato.numero_cartelera, candidato.cantidad_votos, candidato.eleccion_id, candidato.persona_id, candidato.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating candidate: {e}")
    
    async def delete(self, id: int) -> None:
        query = "DELETE FROM candidato WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting candidate: {e}")
    
    async def get_by_id(self, id: int) -> CandidatoDomain:
        query = "SELECT id, numero_cartelera, cantidad_votos, eleccion_id, persona_id FROM candidato WHERE id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                return CandidatoDomain(
                    id=result['id'],
                    numero_cartelera=result['numero_cartelera'],
                    cantidad_votos=result['cantidad_votos'],
                    eleccion_id=result['eleccion_id'],
                    persona_id=result['persona_id']
                )
        except Exception as e:
            print(f"Error fetching candidate by ID: {e}")
            return None
    
    async def get_by_eleccion_id(self, eleccion_id: int) -> list[CandidatoDomain]:
        query = "SELECT id, numero_cartelera, cantidad_votos, eleccion_id, persona_id FROM candidato WHERE eleccion_id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (eleccion_id,))
                result = cursor.fetchall()
                return [
                    CandidatoDomain(
                        id=row['id'],
                        numero_cartelera=row['numero_cartelera'],
                        cantidad_votos=row['cantidad_votos'],
                        eleccion_id=row['eleccion_id'],
                        persona_id=row['persona_id']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching candidates by eleccion ID: {e}")
            return []
    
    async def get_by_persona_id(self, persona_id: int) -> CandidatoDomain:
        query = "SELECT id, numero_cartelera, cantidad_votos, eleccion_id, persona_id FROM candidato WHERE persona_id=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (persona_id,))
                result = cursor.fetchone()
                return CandidatoDomain(
                    id=result['id'],
                    numero_cartelera=result['numero_cartelera'],
                    cantidad_votos=result['cantidad_votos'],
                    eleccion_id=result['eleccion_id'],
                    persona_id=result['persona_id']
                )
        except Exception as e:
            print(f"Error fetching candidate by persona ID: {e}")
            return None
    
    async def get_by_numero_cartelera(self, numero_cartelera: int) -> CandidatoDomain:
        query = "SELECT id, numero_cartelera, cantidad_votos, eleccion_id, persona_id FROM candidato WHERE numero_cartelera=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (numero_cartelera,))
                result = cursor.fetchone()
                return CandidatoDomain(
                    id=result['id'],
                    numero_cartelera=result['numero_cartelera'],
                    cantidad_votos=result['cantidad_votos'],
                    eleccion_id=result['eleccion_id'],
                    persona_id=result['persona_id']
                )
        except Exception as e:
            print(f"Error fetching candidate by numero_cartelera: {e}")
            return None
    
