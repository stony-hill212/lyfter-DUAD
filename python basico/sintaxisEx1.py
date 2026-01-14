retail_price=float(input("Ingrese el precio del producto: "))
if (retail_price>=100):
    retail_price=retail_price*0.90
else:
    retail_price=retail_price*0.98
print("El precio con descuento es: ",retail_price)    
