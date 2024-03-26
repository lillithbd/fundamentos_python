'''
for element in range(1,21):
  print(element)
'''

#recorriendo listas
my_list = [23,45,67,89,43]
for element in my_list:
  print(element)

#recorriendo tuplas
my_tuple= ('lili','juli','mariangel')
for element in my_tuple:
  print(element)

#recorriendo diccionarios
product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
for element in product:
  print(element)

for key in product:
  print(key, '=>', product[key])

for key,value in product.items():
  print(key, '=>', value)

#lista con diccionarios dentro
people = [
  {
    'name': 'lili',
    'age': 39    
  },
  {
    'name': 'juli',
    'age': 10    
  },
  {
    'name': 'santi',
    'age': '70'
  }
]

for person in people:
  print(person)

for person in people:
  print('name =>', person['name'])

