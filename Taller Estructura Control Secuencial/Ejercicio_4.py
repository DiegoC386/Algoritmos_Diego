"""
Entradas
Compra-->int-->Compra
Salidas
Descuento-->int-->Desc
Precio-->int-->Precio
"""
#ENTRADA
Compra=int(input("Ingrese total de la Compra"))
#CAJANEGRA
Desc=Compra*0.15
Precio=Compra-Desc
#SALIDA
print("Cuanto es el descuento: "+str(Desc))
print("El Precio Total a pagar es: "+str(Precio))