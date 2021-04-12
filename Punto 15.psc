Proceso Inicio_Punto15
	Escribir "Ingrese un numero de dos cifras a invertir"
	Leer Numero
	Unidades<-Numero  MOD 10
	Escribir "El valor de las unidades es" " " Unidades
	Residuo<-trunc(Numero/10)
	Escribir "El valor del residuo es" " " Residuo
	Escribir "El numero inverso es" " ", Unidades,Residuo
FinProceso

