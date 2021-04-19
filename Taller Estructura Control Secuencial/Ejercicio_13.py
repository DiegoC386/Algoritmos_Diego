"""
Entradas
Billetes50000-->int-->N1
Billetes20000-->int-->N2
Billetes10000-->int-->N3
Billetes5000-->int-->N4
Billetes2000-->int-->N5
Billetes1000-->int-->N6
Billetes500-->int-->N7
Billetes200-->int-->N8
Salidas
Dinero Banco-->int-->DineroBanco
"""
#ENTRADAS
N1=int(input("Ingrese la cantidad de billetes de 50000: "))
N2=int(input("Ingrese la cantidad de billetes de 20000: "))
N3=int(input("Ingrese la cantidad de billetes de 10000: "))
N4=int(input("Ingrese la cantidad de billetes de 5000: "))
N5=int(input("Ingrese la cantidad de billetes de 2000: "))
N6=int(input("Ingrese la cantidad de billetes de 1000: "))
N7=int(input("Ingrese la cantidad de billetes de 500: "))
N8=int(input("Ingrese la cantidad de billetes de 200: "))
#CAJANEGRA
DineroBanco=((N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*200))
#SALIDA
print("La cantidad de dinero que hay en el banco es: "+str(DineroBanco))