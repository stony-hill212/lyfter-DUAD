time_sec=float(input("Ingrese su tiempo en segundos: "))
if (time_sec<600):
    missing_time=(600-time_sec)
    print("Su tiempo es menor a 10min, le faltan",(round(missing_time)),"segundos, para llegar a 10min.")
elif (time_sec==600):
    print("Su tiempo es de 10min.")
else:
    print("Su tiempo mayor a 10min.")        