"""
Dados los datos A, B, C y D que representan números enteros; escriba
un algoritmo que calcule el resultado de las siguientes expresiones:

"""
A=int(input())
B=int(input())
C=int(input())
D=int(input())
if (D==0):
	E=(A-C)**2
	print(E)
elif D>0:
	F=(((A-B)**3)/D)
	print(F)
else:
	print("No es posible")