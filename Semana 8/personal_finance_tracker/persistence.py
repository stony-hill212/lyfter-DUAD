import csv
from datetime import datetime

file_name="finance_data.csv"
date_format="%d/%m/%Y"

def export_to_csv(movements,totals):
    with open(file_name,"w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["Date","Title","Category","Type","Amount"])
        for m in movements:
            writer.writerow([
                m["date"],
                m["title"],
                m["type"],
                m["amount"]
            ])
        writer.writerow(["TOTAL INCOME", totals["income"]])
        writer.writerow(["TOTAL EXPENSES", totals["expenses"]])
        writer.writerow(["BALANCE", totals["balance"]])

def load_from_csv():
    movements=[]
    try:
        with open(file_name,"r")as file:
            reader=csv.DictReader(file)
            for row in reader:
                if not row["Amount"]:
                    continue
                if row["Date"].startswith("TOTAL"):
                    break
                movements.append({
                    "date":datetime.strptime(row["Date"],date_format),
                    "title":row["Title"].strip().capitalize(),
                    "category":row["Category"].strip().capitalize(),
                    "type":row["Type"].strip().capitalize(),
                    "amount":float(row["Amount"])
                })
    except FileNotFoundError:
        pass
    return movements