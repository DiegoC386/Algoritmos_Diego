"""
Una empresa que comercializa cosméticos tiene organizados a sus vendedores en tres
departamentos y ha establecido un programa de incentivos para incrementar su productividad.
El gerente, al final del mes, pide el importe global de las ventas de los tres
departamentos y aquellos que excedan el 33% de las ventas totales se les paga una
cantidad extra equivalente al 20% de su salario bruto mensual.  Si todos los vendedores
ganan lo mismo, determinar cuánto recibirán los vendedores de los tres departamentos al
finalizar el mes.
"""

Sueldo=200000
Sueldo1=Sueldo
Sueldo2=Sueldo
Sueldo3=Sueldo
Venta1=int(input("Ingrese Venta: "))
Venta2=int(input("Ingrese Venta: "))
Venta3=int(input("Ingrese Venta: "))
TotalVentas=(Venta1+Venta2+Venta3)
SueldoExtra=Sueldo*0.2
if(Venta1>=0.33*TotalVentas):
	Sueldo1=Sueldo+SueldoExtra
else:
	Sueldo1=Sueldo
if(Venta2>=0.33*TotalVentas):
	Sueldo2=Sueldo+SueldoExtra
else:
	Sueldo2=Sueldo
if(Venta3>=0.33*TotalVentas):
	Sueldo3=Sueldo+SueldoExtra
else:
	Sueldo3=Sueldo
print("El Sueldo del primer departamentos es: $ {:.1f}".format(Sueldo1))
print("El Sueldo del segundo departamentos es: $ {:.1f}".format(Sueldo2))
print("El Sueldo del tercer departamentos es: $ {:.1f}".format(Sueldo3))



