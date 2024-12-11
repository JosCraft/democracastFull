from src.core.abstractions.infraestructure.respository.usuario_repository_abstract import IUsuarioRepository
from src.core.models.usuario_domain import UsuarioDomain
import bcrypt

class UsuarioRepository(IUsuarioRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[UsuarioDomain]:
        query = "SELECT id, usuario, password, rol_id, estado_id FROM usuario"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return [
                    UsuarioDomain(
                        id=row['id'], 
                        usuario=row['usuario'], 
                        password=row['password'], 
                        rol_id=row['rol_id'], 
                        estado_id=row['estado_id']
                    ) for row in result
                ]
        except Exception as e:
            print(f"Error fetching all users: {e}")
            return []

    async def create(self, usuario: UsuarioDomain) -> None:
        query = "INSERT INTO usuario (usuario, password, rol_id, estado_id) VALUES (%s, %s, %s, %s)"
        try:
            hashed_password = bcrypt.hashpw(usuario.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            with self.connection.cursor() as cursor:
                print(usuario.usuario)
                cursor.execute(query, (usuario.usuario, hashed_password, usuario.rol_id, 1))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating user: {e}")

    async def update(self, usuario: UsuarioDomain) -> None:
        query = "UPDATE usuario SET usuario=%s, password=%s, rol_id=%s, estado_id=%s WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (usuario.usuario, usuario.password, usuario.rol_id, usuario.estado_id, usuario.id))
                self.connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")

    async def delete(self, id: int) -> None:
        query = "DELETE FROM usuario WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")

    async def login(self, usuario: str, password: str) -> UsuarioDomain | str:
        query = "SELECT * FROM usuario WHERE usuario=%s"
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (usuario,))
                result = cursor.fetchone()
                if not result or not bcrypt.checkpw(password.encode('utf-8'), result['password'].encode('utf-8')):
                    return "Usuario no autenticado"

            update_query = "UPDATE usuario SET estado_id=1 WHERE usuario=%s"
            with self.connection.cursor() as cursor:
                cursor.execute(update_query, (usuario,))
                self.connection.commit()

            return UsuarioDomain(
                id=result['id'],
                usuario=result['usuario'],
                password=result['password'],
                rol_id=result['rol_id'],
                estado_id=result['estado_id']
            )
        except Exception as e:
            print(f"Error during login: {e}")
            return "Usuario no autenticado"

    async def logout(self, id: int) -> None:
        query = "UPDATE usuario SET estado_id=2 WHERE id=%s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id,))
                self.connection.commit()
        except Exception as e:
            print(f"Error during logout: {e}")
