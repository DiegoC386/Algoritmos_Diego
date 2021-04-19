"""
Entradas
Nombre-->int--> Nombre
Numero Hijos-->int--> NH
Sueldo Base-->int--> SB
HorasTrabajadas-->int--> HT
HorasExtras-->int--> HE
Salidas
Deducciones-->int--> DEDUC
Asignaciones-->int--> ASIG
SueldoNeto-->int--> SN
"""
#ENTRADAS
Nombre=input("Ingrese su Nombre: ")
NH=int(input("Ingrese numero de Hijos: "))
SB=int(input("Ingrese Sueldo Base: "))
HT=int(input("Ingrese Horas Trabajadas: "))
HE=int(input("Ingrese Horas Extras: "))
#CAJANEGRA
Dia=(SB/31)
PH=(Dia/8)
Sueldo=HT*PH
HE=((PH*0.25)+PH)
PF=(SB*0.05)
POLH=(SB*0.02)
CDA=(SB*0.07)
DEDUC=(PF+POLH+CDA)
ASIG=((250000)+(173000*(NH)+(180000)))
SN=((Sueldo+ASIG+HE)-DEDUC)
#SALIDA
print("Las Deducciones son: "+str(DEDUC))
print("Las Asignaciones son: "+str(ASIG))
print("El Sueldo Neto es: "+str(SN))