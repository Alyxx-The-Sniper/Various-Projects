import random

print ('\nGuessing Number Game')
name = input('Enter your Name: ')
question = input('Pls input you bet number: ')
# This question is only a disguise only the input value has no relation to the luckyNumber
# because luckyNumber will generate a random number from 1-6
luckyNumber = ''
# luckyNumber is a random number from 1 - 6

luckyNumber = random.randint(1,6)

if luckyNumber == 1:
  print('\nCongratulation!' + name + ' you won 100$!!')
elif  luckyNumber == 2:
  print('\nCongratulation! ' + name + ' you won 200$!!')
elif luckyNumber == 3:
  print('\nCongratulation! ' + name + ' you won 300$!!')
elif luckyNumber == 4:
  print('\nCongratulation! ' + name + ' you won 400$!!')
elif luckyNumber == 5:
  print('\nCongratulation! ' + name + ' you won 500$!!')
else:
  print('Sorry ' + name + 'You loss the draw\n Pls Try Again')


