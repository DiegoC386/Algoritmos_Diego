"""
Entradas
Capital-->int-->Cap
Salidas
DineroInvertido-->int-->DInvertido
DineroGanado-->int-->DGanado
"""
#ENTRADAS
Cap=int(input("Ingrese el Capital a Invertir: "))
#CAJANEGRA
DInvertido=Cap*0.020
DGanado=DInvertido+Cap
#SALIDA
print("El Dinero Invertido es: "+str(DInvertido))
print("El Dinero Ganado a un mes es: "+str(DGanado))