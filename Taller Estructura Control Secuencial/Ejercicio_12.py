"""
Entradas
ExamenMatematicas-->float-->Mate
ExamenFisica-->float-->Fis
ExamenQuimica-->float-->Quim
NotasTareasMatematicas1-->float-->NotaM1
NotasTareasMatematicas2-->float-->NotaM2
NotasTareasMatematicas3-->float-->NotaM3
NotasTareasFisica1-->float-->NotaF1
NotasTareasFisica2-->float-->NotaF2
NotasTareasQuimica1-->float-->NotaQ1
NotasTareasQuimica2-->float-->NotaQ2
NotasTareasQuimica3-->float-->NotasQ3
Salidas
DefinitivaMatematicas-->float-->DefiMate
DefinitiFisica-->float-->DefiFis
DefinitivaQuimica-->float-->DefiQuim
PromedioGeneral-->float-->PromGeneral
PromedioMatematicas-->float-->PromMate
PromedioFisica-->float-->PromFis
PromedioQuimica-->float-->PromQuim
"""
#ENTRADAS
Mate=float(input("Ingrese su nota en el examen de Matematicas: "))
Fis=float(input("Ingrese su nota en el examen de Fisica: "))
Quim=float(input("Ingrese su nota en el examen de Quimica: "))
NotaM1=float(input("Ingrese la primera nota obtenida en las tareas de Matematicas: "))
NotaM2=float(input("Ingrese la segunda nota obtenida en las tareas de Matematicas: "))
NotaM3=float(input("Ingrese la tercera nota obtenida en las tareas de Matematicas: "))
NotaF1=float(input("Ingrese la primera nota obtenida en las tareas de Fisica: "))
NotaF2=float(input("Ingrese la segunda nota obtenida en las tareas de Fisica: "))
NotaQ1=float(input("Ingrese la primera nota obtenida en las tareas de Quimica: "))
NotaQ2=float(input("Ingrese la segunda nota obtenida en las tareas de Quimica: "))
NotaQ3=float(input("Ingrese la tercera nota obtenida en las tareas de Quimica: "))
#CAJANEGRA
ExamMate=(Mate*0.90)
ExamFis=(Fis*0.80)
ExamQuim=(Quim*0.85)
PromTMate=((NotaM1+NotaM2+NotaM3)/3)*0.10
PromTFis=((NotaF1+NotaF2)/2)*0.20
PromTQuim=((NotaQ1+NotaQ2+NotaQ3)/3)*0.15
DefiMate=(ExamMate+PromTMate)
DefiFis=(ExamFis+PromTFis)
DefiQuim=(ExamQuim+PromTQuim)
PromGeneral=((DefiMate+DefiFis+DefiQuim)/3)
PromMate=(DefiMate)/2
PromFis=(DefiFis)/2
PromQuim=(DefiQuim)/2
#SALIDAS
print("La definitiva en Matematicas es: "+str(DefiMate))
print("La definitiva en Fisica es: "+str(DefiFis))
print("La definitiva en Quimica es: "+str(DefiQuim))
print("El Promedio General es: "+str(PromGeneral))
print("El Promedio de Matematicas es: "+str(PromMate))
print("El Promedio de Fisica es: "+str(PromFis))
print("El Promedio de Quimica es: "+str(PromQuim))