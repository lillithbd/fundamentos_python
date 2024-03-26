import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('Computer_wins', computer_wins)
  print('User_wins', user_wins)
  
  userOpt = input('piedra, papel o tijera =>')
  userOpt = userOpt.lower()

  if not userOpt in options:
    print('esta opcion no es válida')
    continue
  
  compOpt = random.choice(options)
  
  print('User Option =>', userOpt)
  print('Computer Option =>', compOpt)
  
  if userOpt == compOpt:
    print('empate')
  elif userOpt == 'piedra':
   if compOpt == 'tijera':
     print('piedra gana a tijera, user ganó')
     user_wins += 1
   else:
     print('papel gana a piedra, computer ganó')
     computer_wins += 1
  elif userOpt == 'papel':
    if compOpt == 'piedra':
     print('papel gana a piedra, user ganó')
     user_wins += 1
    else:
     print('tijera gana a papel, computer ganó')
     computer_wins += 1
  elif userOpt == 'tijera':
    if compOpt == 'papel':
     print('papel gana a tijera, user ganó')
     user_wins += 1 
    else:
     print('piedra gana a tijera, computer ganó')
     computer_wins += 1

  if computer_wins == 2:
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('El ganador es el usuario')
    break
  
  rounds += 1
