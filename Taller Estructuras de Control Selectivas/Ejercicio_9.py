"""
En una tienda efectúan un descuento a los clientes dependiendo del monto de la compra.
El descuento se efectúa con base en el siguiente criterio:
a.	Si el monto es inferior a $50.000 COP, no hay descuento.
b.	Si está comprendido entre $50.000 COP y $100.000 COP inclusive,
se hace un descuento del 5%.
c.	Si está comprendido entre $100.000 COP y $700.000 COP inclusive,
se hace un descuento del 11%.
d.	Si está comprendido entre $700.000 COP y $1.500.000 COP inclusive,
el descuento es del 18.
e.	Si el monto es mayor a $15000, hay un 25% de descuento.
Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar
y descuento recibido.
"""
Nombre=input("Ingrese su nombre: ")
Compra=int(input("Ingrese Precio de la Compra: "))
if(Compra>0 and Compra<50000):
	print("Nombre del cliente: "+ str(Nombre))
	print("Monto de la compra: $ {:.0f}".format(Compra))
	print("No hay descuento")
	print("Monto a Pagar: $ {:.0f}".format(Compra))
elif(Compra>=50000 and Compra<100000):
	Desc=(Compra*0.05)
	MontoPagar=(Compra-Desc)
	print("Nombre del cliente: "+ str(Nombre))
	print("Monto de la compra: $ {:.0f}".format(Compra))
	print("Descuento Recibido: $ {:.0f}".format(Desc))
	print("Monto a Pagar: $ {:.0f}".format(MontoPagar))
elif(Compra>=100000 and Compra<700000):
	Desc=(Compra*0.11)
	MontoPagar=(Compra-Desc)
	print("Nombre del cliente: "+ str(Nombre))
	print("Monto de la compra: $ {:.0f}".format(Compra))
	print("Descuento Recibido: $ {:.0f}".format(Desc))
	print("Monto a Pagar: $ {:.0f}".format(MontoPagar))
elif(Compra>=700000 and Compra<1500000):
	Desc=(Compra*0.18)
	MontoPagar=(Compra-Desc)
	print("Nombre del cliente: "+ str(Nombre))
	print("Monto de la compra: $ {:.0f}".format(Compra))
	print("Descuento Recibido: $ {:.0f}".format(Desc))
	print("Monto a Pagar: $ {:.0f}".format(MontoPagar))
elif(Compra>=1500000):
	Desc=(Compra*0.25)
	MontoPagar=(Compra-Desc)
	print("Nombre del cliente: "+ str(Nombre))
	print("Monto de la compra: $ {:.0f}".format(Compra))
	print("Descuento Recibido: $ {:.0f}".format(Desc))
	print("Monto a Pagar: $ {:.0f}".format(MontoPagar))	
else:
	print("ERROR")


	