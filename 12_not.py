print(not True)
print(not False)

# NOT AND
print(" NOT AND ")
print('True and True =>', not(True and True))
print('True and False =>', not(True and False))
print('False and True =>', not(False and True))
print('False and False =>', not(False and False))


stock = input('Ingrese el número de stock => ')
stock = int(stock)
print(not(stock >= 100 and stock <= 1000))