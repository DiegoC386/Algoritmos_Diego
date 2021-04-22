A, B, C= input ().split ()
A=float(A)
B=float(B)
C=float(C)
Pi=3.14159
Triangulo=(A*C)/2
Circulo=Pi*(C**2)
Trapezio=((A+B)/2)*C
Cuadrado=B*B
Rectangulo=A*B
print("TRIANGULO: {:.3f}".format(Triangulo))
print("CIRCULO: {:.3f}".format(Circulo))
print("TRAPEZIO: {:.3f}".format(Trapezio))
print("CUADRADO: {:.3f}".format(Cuadrado))
print("RECTANGULO: {:.3f}".format(Rectangulo))