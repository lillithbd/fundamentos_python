person = {
  'name': 'lili',
  'last_name': 'bobadilla',
  'langs': ['python','c#'],
  'age': 100
}

print(person)

#actualizar atributo
person['name'] = 'santi'
person['age'] -= 15
person['langs'].append('rust')
print(person)


#eliminar atributo
del person['last_name']
person.pop('age')
print(person)

#obtener items de diccionario
print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())