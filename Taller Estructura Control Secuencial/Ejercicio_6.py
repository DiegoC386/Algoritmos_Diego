"""
Entradas
CantMujeres-->int-->Mujeres
CantHombres-->int-->Hombres
Salidas
PorcentajeMujeres-->int-->PorcM
PorcentajeHombres-->int-->PorcH
"""
#ENTRADA
Mujeres=int(input("Ingrese cantidad de mujeres: "))
Hombres=int(input("Ingrese cantidad de hombres: "))
#CAJANEGRA
Total=Mujeres+Hombres
#SALIDA
print("El porcentaje de mujeres es "+str((Mujeres/Total)*100)) 
print("El porcentaje de hombres es "+str((Hombres/Total)*100)) 
