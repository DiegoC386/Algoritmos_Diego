"""
Desarrolle un programa en Python que calcule y muestre el monto que debe pagar
ar suscriptor por concepto de consumo de luz eléctrica y servicio de
aseo urbano. Dicho monto se calcula multiplicando la diferencia de la
lectura anterior y la lectura actual por el costo de cada Kilovatio hora,
según la siguiente escala:
0 -­ 100-->4.600 COP/ Kwh
101 ­- 300-->80.00 COP/ Kwh
301 – 500 -->100.000 COP /Kwh
501 – en Adelante -->120.000 COP/ Khw
"""
LecturaAnterior=int(input("Ingrese Lectura Anterior: "))
LecturaActual=int(input("Ingrese Lectura Actual: "))
Dif=LecturaActual-LecturaAnterior
if(Dif>0 and Dif<=100):
	MontoPagar=Dif*4.600
	print("Monto a Pagar es:  {:.0f}".format(MontoPagar))
elif(Dif>101 and Dif<=300):
	MontoPagar=Dif*80.00
	print("Monto a Pagar es:  {:.0f}".format(MontoPagar))
elif(Dif>301 and Dif<=500):
	MontoPagar=Dif*100.000
	print("Monto a Pagar es:  {:.0f}".format(MontoPagar))
elif(Dif>501):
	MontoPagar=Dif*120.000
	print("Monto a Pagar es:  {:.0f}".format(MontoPagar))
else:
	print("ERROR")

	