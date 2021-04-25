"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a
un fabricante de refacciones. La empresa dependiendo del monto total de la compra,
decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede
de $5.000.000 COP la empresa tendrá la capacidad de invertir de su propio dinero
un 55 % del monto de la compra, pedir prestamo al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no excede de
$5.000.000 COP la empresa tendrá capacidad de invertir de su propio dinero un 70% y
el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra por
concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
Calcule y muestre la cantidad a invertir de los fondos de la empresa, la cantidad a
pagar a crédito, el monto a pagar por intereses y si es necesario la cantidad prestada
al banco.
"""

Piezas=int(input())
CostoPiezas=int(input())
Total=Piezas*CostoPiezas
if (Total>5000000):
	Invertir=Total*0.55
	Prestamo=Total*0.30
	Credito=Total*0.15
	Intereses=Credito*0.20
	print("Cantidad a Invertir: $ {:.1f}".format(Invertir))
	print("Cantidad de Prestamo: $ {:.1f}".format(Prestamo))
	print("Cantidad a Credito: $ {:.1f}".format(Credito))
	print("Intereses: $ {:.1f}".format(Intereses))
elif (Total>0 and Total<5000000):
	Invertir=Total*0.70
	Prestamo=0
	Credito=Total*0.30
	Intereses=Credito*0.20
	print("Cantidad a Invertir: $ {:.1f}".format(Invertir))
	print("Cantidad de Prestamo: $ {:.1f}".format(Prestamo))
	print("Cantidad a Credito: $ {:.1f}".format(Credito))
	print("Intereses: $ {:.1f}".format(Intereses))
else:
	print("Error al digitar")

	