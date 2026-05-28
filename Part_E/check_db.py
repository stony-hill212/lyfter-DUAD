import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from shared_db.main_db import get_connection

TABLES=["users", "vehicles", "rentals"] 

def check_tables(cursor):
    for table in TABLES:
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_name= %s           
            )
        """, (table,))
        exists=cursor.fetchone()["exists"]
        if not exists:
            return False, f"DB ERROR. Table '{table}' does not exist"
    return True, "All tables exist"

def available_vehicles(cursor):
    cursor.execute("""
        SELECT COUNT(*) AS available_count
        FROM vehicles
        WHERE vehicle_status= 'available'
    """)
    result=cursor.fetchone()
    if result["available_count"]<1:
        return False, "DB ERROR. No vehicles available"
    return True, "Vehicles available"

def main():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        tables_ok, tables_message=check_tables(cursor)
        if not tables_ok:
            print(tables_message)
            return
        vehicles_ok, vehicles_message=available_vehicles(cursor)
        if not vehicles_ok:
            print(vehicles_message)
            return
        print("DB OK, system running smoothly")
    except Exception as error:
        print(f"DB CONNECTION ERROR: {error}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()

if __name__=="__main__":
    main()