"""
Entradas
PrecioArticulo-->int-->PArt
CuotasMensuales-->int-->NCuo
Recargo-->float-->Rec
Salidas
PorcentajeporCantidadCuotas-->float-->PvCuota
"""
#ENTRADAS
PArt=int(input("Ingrese e Precio del Articulo: "))
Ncuo=int(input("Ingrese Numero de Cuotas: "))
Rec=float(input("Ingrese el Pocentaje del Recargo: "))
#CAJANEGRA
VMen=(PArt/Ncuo)
VRec=((VMen)*(Rec/100))
Vcuota=(VMen+VRec)
Vcuo=(Vcuota*Ncuo)
PvCuota=((PArt*100)/Vcuo)
#SALIDAS
print("Porcentaje a cobrar en la cantidad de cuotas es: "+str(PvCuota))
