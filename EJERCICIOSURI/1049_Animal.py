x = input()
y = input()
z = input()

if (x == 'vertebrado' and y == 'ave' and z == 'carnivoro'):
    animal = 'aguia'
elif (x == 'vertebrado' and y == 'ave' and z == 'onivoro'):
    animal = 'pomba'
elif (x == 'vertebrado' and y == 'mamifero' and z == 'onivoro'):
    animal = 'homem'
elif (x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro'):
    animal = 'vaca'
elif (x == 'invertebrado' and y == 'inseto' and z == 'hematofago'):
    animal = 'pulga'
elif (x == 'invertebrado' and y == 'inseto' and z == 'herbivoro'):
    animal = 'lagarta'
elif (x == 'invertebrado' and y == 'anelideo' and z == 'hematofago'):
    animal = 'sanguessuga'
elif (x == 'invertebrado' and y == 'anelideo' and z == 'onivoro'):
    animal = 'minhoca'
else:
    print(animal)