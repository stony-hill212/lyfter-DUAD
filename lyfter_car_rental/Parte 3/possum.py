import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="jackrabbit_db",
        user="postgres",
        password="Sierramadre08"
    )