"""
Entradas
LotesNaranja-->int-->X
DocenasNaranja-->int-->Y
ValorVenta-->int-->K
Salidas
PorcentajeGanancias-->float-->Porc
"""
#ENTRADAS
X=int(input("Ingrese cantidad de Lotes de naranjas: "))
Y=int(input("Ingrese Precio por Docenas de naranjas: "))
K=int(input("Ingrese Valor de Venta: "))
#CAJANEGRA
NumDoc=(X/12)
Cost=(Y*NumDoc)
Ganancia=(K-Cost)
Porc=(Ganancia/Cost)*100
#SALIDA
print("El porcentaje de Ganancias es: " +str(Porc))