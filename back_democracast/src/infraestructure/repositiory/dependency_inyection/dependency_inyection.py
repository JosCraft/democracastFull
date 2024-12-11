from fastapi import Depends
from src.infraestructure.repositiory.connection import get_connection


def get_db_connection():
    connection = get_connection()
    try:
        yield connection
    finally:
        connection.close()
