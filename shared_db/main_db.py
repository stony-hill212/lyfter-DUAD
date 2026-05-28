import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="jackrabbit_db",
        user="postgres",
        password="Sierramadre08",
        cursor_factory=RealDictCursor
    )