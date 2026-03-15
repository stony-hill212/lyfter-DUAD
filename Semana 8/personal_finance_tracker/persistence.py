import csv
import os
from datetime import datetime

file_name="finance_data.csv"
date_format="%d/%m/%Y"

def append_to_csv(movement,target=file_name):
    with open(target,"a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([
            movement.date.strftime(date_format),
            movement.title,
            movement.category.name,
            movement.movement_type,
            movement.amount
        ])

def initialize_csv(target=file_name):
    if os.path.exists(target):
        return
    with open(target,"w",newline="",encoding="utf-8")as file:
        writer=csv.writer(file)
        writer.writerow(["Date","Title","Category","Type","Amount"])

def load_from_csv(target=file_name):
    movements=[]
    try:
        with open(target,"r",newline="",encoding="utf-8")as file:
            reader=csv.DictReader(file)
            if not reader.fieldnames:
                return []
            for row in reader:
                if not row.get("Amount"):
                    continue
                if row.get("Date","").startswith("TOTAL"):
                    break
                date_str=row.get("Date")
                try:
                    date=datetime.strptime(date_str,date_format)
                except ValueError:
                    date=datetime.fromisoformat(date_str)
                movements.append({
                    "date":date,
                    "title":row.get("Title","").strip(),
                    "category":row.get("Category").strip(),
                    "type":row.get("Type","").strip(),
                    "amount":float(row.get("Amount"))
                })
    except FileNotFoundError:
        return []
    return movements

def export_to_csv(movements,totals,target=file_name):
    with open(target,"w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["Date","Title","Category","Type","Amount"])
        for m in movements:
            writer.writerow([
                m.date.strftime(date_format),
                m.title,
                m.category.name,
                m.movement_type,
                m.amount
            ])
        writer.writerow(["TOTAL INCOME", totals["income"]])
        writer.writerow(["TOTAL EXPENSES", totals["expenses"]])
        writer.writerow(["BALANCE", totals["balance"]])

