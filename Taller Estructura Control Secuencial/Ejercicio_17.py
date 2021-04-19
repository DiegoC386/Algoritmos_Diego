"""
Entradas
PresupuestoAnual-->int-->PA
Salidas
PresupuestoGinecologia-->int-->PG
PresupuestoTraumatogia-->int-->PT
PresupuestoPediatria-->int-->PP
"""
#ENTRADAS
PA=int(input("Ingrese Presupuesto Anual: "))
#CAJANEGRA
PG=PA*0.4
PT=PA*0.3
PP=PA*0.3
#SALIDAS
print("El Dinero que recibe el area de Ginecología es: " +str(PG))
print("El Dinero que recibe el area de Traumatología es: " +str(PT))
print("El Dinero que recibe el area de Pediatría es: " +str(PP))