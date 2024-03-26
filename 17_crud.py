#CRUD Create, Read, Update, Delete
#Create
numbers = [1,2,3,4,5]

#Read
print(numbers[1])

#Update
numbers[-1] = 10
print(numbers)

#Agregar elemento al final de la lista
numbers.append(700)
print(numbers)

#Agregar elementos en otras posiciones de la lista
numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

#Fusionar listas
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

#Buscar un valor específico, saber en qué posición está y actualizarlo
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#Delete
new_list.remove('todo 1')
print(new_list)

#eliminar el último elemento de la lista
new_list.pop()
print(new_list)

#eliminar el elemento determinado en la posición específica
new_list.pop(0)
print(new_list)

#Voltear todo el array
new_list.reverse()
print(new_list)

#Ordenar
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()