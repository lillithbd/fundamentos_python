text = 'Ella sabe programar en Python'

'''
#busqueda de texto
print('JavaScript' in text)
print('Python' in text)


if ('JS' in text):
  print('Elegiste bien.')
else:
  print('También elegiste bien')
'''

#tamaño 
size = len(text)
print(size)

#mayúsculas y minúsculas
print(text)
print(text.upper())
print(text.lower())

#contar cuántas veces aparece un texto dentro de otro
print(text.count('a'))

#transformar mayúsculas a minúsculas y viceversa
print(text.swapcase())

#valida si un texto inicia con algo específico
print(text.startswith('Ella'))

#valida si un texto termina con algo específico
print(text.endswith('Rust'))

#reemplazar texto
print(text.replace('Python', 'Go'))

#Poner primer caracter en mayúscula
text2 = 'este es un título'
print(text2)
print(text2.capitalize())

#Poner el inicio de cada palabra en mayúscula
print(text2.title())

#Valida si el texto es un dígito
print(text2.isdigit())
print("398".isdigit())
