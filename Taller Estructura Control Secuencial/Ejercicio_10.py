"""
Entradas
Chelines Austriacos-->int-->CA
Dracmas Griegos-->int-->DG
Pesetas-->int-->Pes
Salidas
Pesetas-->int-->P
FrancoFrances-->int-->FF
Dolares-->int-->D
LirasItalianas-->int-->LI
"""
#ENTRADA
CA=int(input("Ingrese la cantidad de Chelines Austriacos a cambiar: "))
DG=int(input("Ingrese la cantidad de Dracmas Griegos a cambiar: "))
Pes=int(input("Ingrese la cantidad de pesetas a cambiar: "))
#CAJANEGRA
P=(CA*9856871)/100
FF=((DG*88607)/100)*(1/20110)
D=Pes/122499
LI=(Pes*100)/9289
#SALIDA
print("La cantidad de Chelines Austriacos a Pesetas es: "+"{:.3f}".format(P))
print("La cantidad de Dracmas Griegos a Franco Frances es: "+"{:.3f}".format(FF))
print("La cantidad de Pesetas a Dolares es: "+"{:.3f}".format(D))
print("La cantidad de Pesetas a Liras Italianas es: "+"{:.3f}".format(LI))