"""
Entradas
MesAnterior-->int-->MAN
KilovatiosMesAnterior-->int-->KWMA
LecturaActual-->int-->KWMAC
Salidas
ValorPagar-->int-->PA
"""
#ENTRADAS
MAN=int(input("Ingrese valor pagado en el Mes Anterior: "))
KWMA=int(input("Ingrese Kilovatios gastados en el Mes Anterior: "))
KWMAC=int(input("Ingrese Lectura Actual de Kilovatios: "))
#CAJANEGRA
P=(KWMA/MAN)
PA=(P*KWMAC)
#SALIDAS
print("El valor a pagar en el Mes Actual es:" +str(PA))