numbers = (1,2,3,4)
strings = ('nico', 'zule', 'santi')

print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#CRUD
#no se puede insertar
#numbers.append(10)
#print(numbers)

#no se puede actualizar
#numbers[1] = 'change'
print(numbers)


print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

#convertir tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

False or True 
