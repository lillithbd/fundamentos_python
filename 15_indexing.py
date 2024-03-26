text = 'Ella sabe Python'
##Indexing
print(text[0])
print(text[1])

##conocer cuál es el último caracter del texto
#forma 1
size = len(text)
print('size => ', size)
print(text[size - 1])

#forma 2
print(text[-1])

#Slicing
print(text[0:5])
print(text[10:16])

#Desde el inicio hasta un punto determinado
print(text[:10])

#Desde el caracter 5 hasta el final
print(text[5:])

#Desde el inicio hasta el final
print(text[:])

#saltos entre textos
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])