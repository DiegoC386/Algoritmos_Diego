Proceso Inicio_Punto11
	Escribir "Escriba la calificación de los tres parciales"
	Leer Nota1,Nota2,Nota3
	Escribir "Escriba la calificación del examen final"
	Leer Nota4
	Escribir "Escriba la calificación de un trabajo final"
	Leer Nota5
	Promedio<-(Nota1+Nota2+Nota3)/3
	NotaFinal1<-Promedio*0.55
	NotaFinal2<-Nota4*0.3
	NotaFinal3<-Nota5*0.15
	Definitiva<-(NotaFinal1+NotaFinal2+NotaFinal3)
	Escribir "La definitiva en la materia de Algoritmos es" " " Definitiva
FinProceso
