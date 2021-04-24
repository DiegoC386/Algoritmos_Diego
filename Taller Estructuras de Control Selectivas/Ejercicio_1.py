""""
Un hombre desea saber cuánto dinero se generará por concepto de intereses
sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir
los intereses siempre y cuando éstos excedan a $100.000 COP y en ese caso,
desea saber cuánto dinero tendrá finalmente en su cuenta.
"""
Cap=int(input())
InvBan=float(input())
Int=(InvBan/100)*Cap
if (Int>=100000):
	Capf= Cap+Int
	print(Capf)
else:
	print("No invertir")

	