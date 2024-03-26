my_dict = {}
print(type(my_dict))

my_dict = {
  'name': 'Nicolas',
  'lastname' : 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

#leer atributos dentro del diccionario
print(my_dict['age'])
print(my_dict['lastname'])
print(my_dict.get('age'))
print(my_dict.get('unvalor'))

#buscar valores en diccionarios
print('name' in my_dict)
print('otroqueno' in my_dict)