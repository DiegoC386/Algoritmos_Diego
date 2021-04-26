"""
Una compañía de alquiler de automóviles sin conductor, desea calcular y mostrar
lo que debe pagar cada cliente, de acuerdo a las siguientes condiciones:
"""
Km=int(input("Ingrese Kilometros recorridos: "))
if(Km>0 and Km<300):
	Paga=50000
	print("Total a pagar es: $ {:.0f}".format(Paga))
elif(Km>300 and Km<1000):
	Total=(((1000-Km)*30000)+70000)
	print("Total a pagar es: $ {:.0f}".format(Total))
elif(Km>1000):
	Total1=(((Km-1000)*9000)+150000)
	print("Total a pagar es: $ {:.0f}".format(Total1))
else:
	print("No debe pagar nada")

	