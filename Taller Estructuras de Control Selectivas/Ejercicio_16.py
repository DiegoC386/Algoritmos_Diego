"""
Confeccionar un algoritmo que permita resolver una ecuación de segundo grado, de la
forma: AXˆ2+BX+C = 0, sabiendo que el discriminante (D) se calcula con la
fórmula: D= Bˆ2-­4*A*C. El valor obtenido se evalúa y se aplica la fórmula correspondiente,
según muestra la siguiente tabla:
"""
import math
A=int(input("Ingrese valor: "))
B=int(input("Ingrese valor: "))
C=int(input("Ingrese valor: "))
Dis=((B**2)-(4*A*C))
if(Dis == 0):
	X1=(-B/(2*A))
	X2=(-B/(2*A))
	print("Los valores de X1 y X2 son: "+ ' {} y {}'.format(X1, X2))
elif(Dis>0):
	X2=(-B+math.sqrt((B**2)-(4*A*C)))/(2*A)
	X3=(-B-math.sqrt((B**2)-(4*A*C)))/(2*A)
	print("Los valores de X2 y X3 son: "+ ' {} y {}'.format(X2, X3))
elif(Dis<0):
	print("No tiene solución en los reales")
else:
	print("ERROR")

	