"""
Entradas
CantMetros-->float-->M
Salidas
Pulgadas-->float-->In
Pies-->float-->ft
"""
#ENTRADAS
M=float(input("Ingrese cantidad de Metros: "))
#CAJANEGRA
In=M*39.27
Ft=In*12
print("La cantidad de pulgadas es: "+"{:.2f}".format(In))
print("La cantidad de pies es: "+"{:.2f}".format(Ft))
