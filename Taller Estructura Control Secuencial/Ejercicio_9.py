"""
Entradas
Sueldo Base-->int-->SB
HorasTrabajadas-->float-->HT
Salidas
Salario Neto-->int-->SN
"""
#ENTRADAS
SB=int(input("Ingrese Sueldo Base: "))
HT=float(input("Ingrese Horas Trabajadas: "))
#CAJANEGRA
Imp=SB*0.20
C=(SB-Imp)
PD=(C/30)
PH=(PD/8)
SN=(PH*HT)
#SALIDA
print("El salario Neto es: "+str(SN))