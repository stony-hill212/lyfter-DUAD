import csv
import os
def count_by_gender():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(base_dir,"juegos1.csv")
    gender_counter={}
    try:
        with open(file_path,"r",encoding="utf-8")as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                gender=row[1].strip()
                if gender in gender_counter:
                    gender_counter[gender]+=1
                else:
                    gender_counter[gender]=1
        print("Generos encontrados:")
        for gender, count in gender_counter.items():
            print(f"{gender}: {count}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error:", e) 

count_by_gender()                                   