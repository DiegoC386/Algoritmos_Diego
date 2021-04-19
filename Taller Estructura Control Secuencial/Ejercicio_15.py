"""
Entradas
PrecioProducto-->int-->PDP
PrecioPagado-->int-->PFP
Salidas
PorcentajeAplicado-->float-->DESC
DineroAhorrado-->int-->DA
"""
#ENTRADAS
PDP=int(input("Ingrese Precio del Producto: "))
PFP=int(input("Ingrese Precio Final Pagado por el Producto: "))
#CAJANEGRA
DESC=((PFP*100)/PDP)
DA=(PDP-PFP)
#SALIDA
print("El Porcentaje Aplicado es: " +str(DESC))
print("El Dinero Ahorrado es:" +str(DA))