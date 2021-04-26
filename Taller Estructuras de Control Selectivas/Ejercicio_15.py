"""
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
un médico determina si una persona tiene anemia o no, lo cual depende de su nivel
de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina
que tiene una persona es menor que el rango que le corresponde,
se determina su resultado como positivo y en caso contrario como negativo.
La tabla en la que el médico se basa para obtener el resultado es la siguiente:
"""
Edad=int(input ("Ingresa edad en meses: "))
Nivel=float(input ("Ingresa nivel hemoglobina: "))
Genero=int(input("Digite 1 si es Hombre o 2 si es Mujer: "))
if((Edad>1 and Edad<=6) and (Nivel<10.0)):
  print ("Positivo para Anemia")
elif((Edad>1 and Edad<=6)and (Nivel>=10.0)):
  print ("Negativo para Anemia")
elif((Edad>6 and Edad<=12) and (Nivel<11.0)):
  print ("Positivo para Anemia")
elif((Edad>6 and Edad<=12)and (Nivel>=11.0)):
  print ("Negativo para Anemia")
elif((Edad>12 and Edad<=60) and (Nivel<11.5)):
  print ("Positivo para Anemia")
elif((Edad>12 and Edad<=60)and (Nivel>=11.5)):
  print ("Negativo para Anemia")
elif((Edad>60 and Edad<=120) and (Nivel<12.6)):
  print ("Positivo para Anemia")
elif((Edad>60 and Edad<=120)and (Nivel>=12.6)):
  print ("Negativo para Anemia")
elif((Edad>120 and Edad<=180) and (Nivel<13.0)):
  print ("Positivo para Anemia")
elif((Edad>120 and Edad<=180)and (Nivel>=13.0)):
  print ("Negativo para Anemia")
elif((Edad>180 and  Genero==1) and (Nivel<12.0)):
  print ("Positivo para Anemia")
elif((Edad>180 and  Genero==1)and (Nivel>=12.0)):
  print ("Negativo para Anemia")
elif((Edad>180 and  Genero==1) and (Nivel<14.0)):
  print ("Positivo para Anemia")
elif((Edad>180 and  Genero==0)and (Nivel>=14.0)):
  print ("Negativo para Anemia")
else:
	print("ERROR")