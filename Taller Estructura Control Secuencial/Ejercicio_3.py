"""
Entradas
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->v3
sueldobase-->float-->Sb
salidas
comision-->float-->C
total-->float-->Total
"""
#ENTRADA
V1=float(input("Ingrese la venta 1: "))
V2=float(input("Ingrese la venta 2: "))
V3=float(input("Ingrese la venta 3: "))
Sb=float(input("Ingrese Suelo base: "))
#CAJANEGRA
C=((V1+V2+V3)/3)*0.10
Total=Sb+C
#SALIDA
print("La Comision es: "+str(C),"Sueldo Total: "+str(Total))