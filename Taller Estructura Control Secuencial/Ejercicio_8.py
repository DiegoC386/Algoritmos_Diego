"""
Entradas
LongitudLado1-->float-->Lado1
LongitudLado2-->float-->Lado2
LongitudLado3-->float-->Lado3
Salidas
Semiperimetro-->float-->S
Area-->float-->A
"""
import math
#ENTRADA
Lado1=float(input("Ingrese la longitud del primer lado: "))
Lado2=float(input("Ingrese la longitud del segundo lado: "))
Lado3=float(input("Ingrese la longitud del tercer lado: "))
#CAJANEGRA
S=(Lado1+Lado2+Lado3)/2
A=math.sqrt(S*(S-Lado1)*(S-Lado2)*(S-Lado3))
print("El Semiperimetro es: "+str(S))
print("El Area del triangulo es: "+"{:.3f}".format(A))