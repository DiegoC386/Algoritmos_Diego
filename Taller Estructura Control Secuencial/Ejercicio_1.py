"""
Entradas
Per1-->int-->Edad1
Per2-->int-->Edad2
Per3-->int-->Edad3
Salidas
Promedio-->float-->PromEdad
"""
#ENTRADAS
Edad1=int(input("Digite la primera edad: "))
Edad2=int(input("Digite la segunda edad: "))
Edad3=int(input("Digite la tercera edad: "))
#CAJA NEGRA
PromEdad=int((Edad1+Edad2+Edad3)/3)
#SALIDA
print("La Edad Promedio es: "+str(PromEdad))