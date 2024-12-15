from src.core.abstractions.infraestructure.respository.voto_repository_abstract import IVotoRepository  
from src.core.models.voto_domain import VotoDomain

class VotoRepository(IVotoRepository):

    def __init__(self, connection):
        self.connection = connection
    
    async def get_all(self) -> list[VotoDomain]:
        query = "SELECT id, usuario_id, eleccion_id, candidato_id, numero_votos FROM voto"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    VotoDomain(
                        id=row['id'],
                        user_id=row['usuario_id'],
                        eleccion_id=row['eleccion_id'],
                        candidato_id=row['candidato_id'],
                        numero_votos=row['numero_votos']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all votes: {e}")
        
    async def create(self, voto: VotoDomain) -> None:
        query = "INSERT INTO voto (usuario_id, eleccion_id, candidato_id, numero_votos) VALUES (%s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (voto.user_id, voto.eleccion_id, voto.candidato_id, voto.numero_votos))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating vote: {e}")
    
    async def update(self, voto: VotoDomain) -> None:
        query = "UPDATE voto SET usuario_id=%s, eleccion_id=%s, candidato_id=%s, numero_votos=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (voto.user_id, voto.eleccion_id, voto.candidato_id, voto.numero_votos, voto.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating vote: {e}")
    
    async def delete(self, id: int) -> None:
        query = "DELETE FROM voto WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting vote: {e}")
            
