pers_name=(input("Ingrese su nombre completo: "))
pers_age=int(input("Ingrese su edad: "))
if(pers_age<=5):
    print("Usted",pers_name,",es un bebé.")
elif(pers_age<=12):
    print("Usted",pers_name,",es un niño.")
elif(pers_age<=15):
    print("Usted",pers_name,",es un preadolescente.")
elif(pers_age<=17):
    print("Usted",pers_name,",es un adolescente.")
elif(pers_age<=30):
    print("Usted",pers_name,",es un adulto joven.")
elif(pers_age<=65):
    print("Usted",pers_name,",es un adulto.")
else:
    print("Usted",pers_name,",es un adulto mayor.")                
