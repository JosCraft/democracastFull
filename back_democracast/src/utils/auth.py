import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta

# Constantes para configuración del token
SECRET_KEY = "XrkLgy5qnB"  
ALGORITHM = "HS256"
EXPIRATION_HOURS = 5  # Tiempo de expiración en horas

def generar_token(usuario_id: int, nombre: str, rol: str) -> str:
    """
    Genera un token JWT para un usuario.
    
    Args:
        usuario_id (int): ID del usuario.
        nombre (str): Nombre del usuario.
        rol (str): Rol del usuario.
    
    Returns:
        str: Token JWT generado.
    """
    try:
        # Payload del token
        payload = {
            "sub": str(usuario_id),  # Asegura que sea un string
            "nombre": nombre,
            "rol": rol,
            "exp": datetime.utcnow() + timedelta(hours=EXPIRATION_HOURS)  # Tiempo de expiración
        }
        # Generar y devolver el token JWT
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    except Exception as e:
        raise RuntimeError(f"Error al generar el token: {e}")
