amount_gr=int(input("Ingrese la catidad de notas: "))
approved_gr=0
failed_gr=0
approved_ave=0
failed_ave=0
total_ave=0
for i in range(amount_gr):
    if i==0:
        current_gr=float(input("Ingrese la primer nota: "))
    else:
        current_gr=float(input("Ingrese la siguiente nota: "))
    if (current_gr>=70):
        approved_gr=approved_gr+1
        approved_ave=(approved_ave+current_gr) 
        total_ave=total_ave+(current_gr/amount_gr)
        approved_ave=approved_ave/approved_gr
    else:
        failed_gr=failed_gr+1
        failed_ave=(failed_ave+current_gr)
        failed_ave=failed_ave/failed_gr   
print("El estudiante tiene esta cantidad de notas aprovadas: ",approved_gr)
print("Este es el promedio de notas aprobadas: ",approved_ave)
print("El estudiante tiene esta cantidad de notas desaprobadas: ",failed_gr)
print("Este es el promedio de notas desaprobadas: ",failed_ave)
print("Este es el promedio total de notas: ",total_ave)           


    
    

