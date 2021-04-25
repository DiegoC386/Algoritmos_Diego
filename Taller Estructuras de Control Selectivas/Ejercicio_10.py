"""
Construya un programa en Python que, dados como datos la categoría y el sueldo bruto
del trabajador, calcule el aumento correspondiente teniendo en cuenta la siguiente tabla:
Como salida, mostrar la categoría del trabajador y su nuevo sueldo bruto.
"""
SueldoBruto=int(input("Ingrese Sueldo Bruto: "))
if(SueldoBruto<=900000 ):
	NuevoSueldo= (SueldoBruto*0.6)+SueldoBruto
	print("Su Nuevo Sueldo es: $ {:.0f}".format(NuevoSueldo))
	print("Su Categoria es la 5")
elif(SueldoBruto>900000 and SueldoBruto<=2000000):
	NuevoSueldo= (SueldoBruto*0.4)+SueldoBruto
	print("Su Nuevo Sueldo es: $ {:.0f}".format(NuevoSueldo))
	print("Su Categoria es la 4")
elif(SueldoBruto>2000000 and SueldoBruto<=3600000):
	NuevoSueldo= (SueldoBruto*0.2)+SueldoBruto
	print("Su Nuevo Sueldo es: $ {:.0f}".format(NuevoSueldo))
	print("Su Categoria es la 3")
elif(SueldoBruto>3600000 and SueldoBruto<=4300000):
	NuevoSueldo= (SueldoBruto*0.15)+SueldoBruto
	print("Su Nuevo Sueldo es: $ {:.0f}".format(NuevoSueldo))
	print("Su Categoria es la 2")
elif(SueldoBruto>4300000 and SueldoBruto<=5000000):
	NuevoSueldo= (SueldoBruto*0.10)+SueldoBruto
	print("Su Nuevo Sueldo es: $ {:.0f}".format(NuevoSueldo))
	print("Su Categoria es la 1")
else:
	print("No se puede calcular")

	