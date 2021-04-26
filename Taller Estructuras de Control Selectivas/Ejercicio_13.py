"""
Desarrolle un algoritmo que reciba como dato de entrada la fecha de nacimiento
de una persona y a continuación escriba el nombre del signo del zodiaco
correspondiente; así como su edad. Considere la siguiente tabla de signos:
"""
Dia=int(input("Digite Día de Nacimiento: "))
Mes=int(input("Digite Mes de Nacimiento: "))
Año=int(input("Digite Año de Nacimiento: "))
MesActual=int(input("Digite Mes Actual: "))
AñoActual=int(input("Digite Año Actual: "))
MesEdad=MesActual-Mes
Edad=AñoActual-Año
if(MesEdad<0):
	Edad=Edad-1
else:
	Edad=Edad
if(Dia>=22 and Mes==11) or (Dia<=21 and Mes==12):
	Signo="Sagitario"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=22 and Mes==12) or (Dia<=20 and Mes==1):
	Signo="Capricornio"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=21 and Mes==1) or (Dia<=19 and Mes==2):
	Signo="Acuario"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=20 and Mes==2) or (Dia<=19 and Mes==3):
	Signo="Piscis"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=21 and Mes==3) or (Dia<=20 and Mes==4):
	Signo="Aries"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=21 and Mes==4) or (Dia<=19 and Mes==5):
	Signo="Tauro"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=22 and Mes==5) or (Dia<=21 and Mes==6):
	Signo="Geminis"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=22 and Mes==6) or (Dia<=22 and Mes==7):
	Signo="Cancer"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=23 and Mes==7) or (Dia<=23 and Mes==8):
	Signo="Leo"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=24 and Mes==8) or (Dia<=22 and Mes==9):
	Signo="Virgo"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=23 and Mes==9) or (Dia<=22 and Mes==10):
	Signo="Libra"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
elif(Dia>=23 and Mes==10) or (Dia<=21 and Mes==11):
	Signo="Escorpion"
	print("Su Signo Zodiacal es: " +str(Signo))
	print("Su edad es: " +str(Edad) +" años")
else:
	print("ERROR")

