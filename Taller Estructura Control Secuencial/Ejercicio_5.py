"""
Entradas
NotaParcial1-->float-->N1
NotaParcial2-->float-->N2
NotaParcial3-->float-->N3
ExamenFinal-->float-->N4
TrabajoFinal-->float-->N5
Salidas
Definitiva-->float-->Definitiva
"""
#ENTRADAS
N1=float(input("Digite la calificación del primer parcial"))
N2=float(input("Digite la calificación del segundo parcial"))
N3=float(input("Digite la calificación del tercer parcial"))
N4=float(input("Digite la calificación del Examen Final"))
N5=float(input("Digite la calificación del Trabajo Final"))
#CAJANEGRA
Prom=(N1+N2+N3)/3
NotaF1=Prom*0.55
NotaF2=N4*0.3
NotaF3=N5*0.15
#SALIDA
Definitiva=(NotaF1+NotaF2+NotaF3)
print("La definitiva en la materia de Algoritmos es "+str(Definitiva))
