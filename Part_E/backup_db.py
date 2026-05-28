import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from datetime import datetime

from shared_db.main_db import get_connection

TABLES=["users", "vehicles", "rentals"]

def backup_table(cursor, table_name, backup_folder):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows=cursor.fetchall()
    if not rows:
        print(f"No data found in {table_name}")
        return
    file_path=os.path.join(backup_folder, f"{table_name}_backup_{datetime.now().date()}.csv")
    with open(file_path, "w", newline="", encoding="utf-8")as csv_file:
        writer=csv.writer(csv_file)
        headers=rows[0].keys()
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row.values())
    print(f"Backup created: {file_path}")

def main():
    conn=get_connection()
    cursor=conn.cursor()
    backup_folder="db_backups"
    os.makedirs(backup_folder, exist_ok=True)
    for table in TABLES:
        backup_table(cursor, table, backup_folder)
    cursor.close()
    conn.close()
    print("Database backup completed successfully")

if __name__=="__main__":
    main()