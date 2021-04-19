"""
Entradas
Galones-->float-->GAL
Salidas
Litros-->float-->L
PrecioLitros-->int-->PL
"""
#ENTRADAS
GAL=int(input("Ingrese cantidad de Galones: "))
#CAJANEGRA
L=GAL*3.785
PL=L*50000
#SALIDAS
print("La cantidad de litros es: " +str(L))
print("El precio en litros es: " +str(PL))