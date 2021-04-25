"""
Dados los datos A, B, C y D que representan números enteros; escriba
un algoritmo que calcule el resultado de las siguientes expresiones:

"""
A=int(input("Ingrese primer numero: "))
B=int(input("Ingrese segundo numero: "))
C=int(input("Ingrese tercer numero: "))
D=int(input("Ingrese cuarto numero: "))
if (D==0):
	E=(A-C)**2
	print(E)
elif D>0:
	F=(((A-B)**3)/D)
	print(F)
else:
	print("No es posible")

	