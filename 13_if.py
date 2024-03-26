if True:
  print('Debería ejecutarse')

if False:
  print('Nunca se ejecuta')


pet =input('¿Cuál es tu mascota favorita?')

if pet == 'perro':
  print('espero tengas suerte')

elif pet == 'gato':
  print('tienes buen gusto')
elif pet == 'pez':
  print('eres lo máximo')
else:
  print('no tienes ninguna mascota interesante')

'''
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('El stock es correcto')
else:
  print('El stock es incorrecto')
'''

#Ejercicio Par
number = int(input('Ingrese un número => '))
result = number % 2

if (result == 0):
  print('Es par')
else:
  print('Es impar')


