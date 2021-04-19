"""
Entradas
ValorPrestamo-->int-->VP
TasaIntereses-->float-->DTI
NumeroAños-->int-->T
Salidas
PorcentajeCobrado-->float-->PC
"""
#ENTRADAS
VP=int(input("Ingrese el Valor del Prestamo en Bs: "))
TI=float(input("Ingrese el % de la tasa de interes: "))
T=int(input("Ingrese numero de años correspondiente a revisar"))
#CAJANEGRA
Intereses=((VP*(T)*(TI/100))/(100*4))
#SALIDAS
print("El porcentaje cobrado en la cantidad de años es: " +str(Intereses))