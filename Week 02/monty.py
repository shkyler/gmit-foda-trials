#Monty Hall Game
import numpy as np 

doors = ['green', 'blue', 'red']
car = np.random.choice(doors)

print('There is a car behind one of the doors, please pick red, green or blue')
pick = input('Please pick a door!')
while pick not in doors:
    pick = input("Please pick a valid door!")

show = np.random.choice([door for door in doors if door !=pick and door !=car])

print("I can now reveal to you that there is no car behind the " + show + " door")

otherdoor = np.random.choice([door for door in doors if door !=pick and door !=show])

stay = input("Would you like to stay with your original door or switch?")

while stay not in ['stay', 'switch']:
    stay = input ("Would you like to stay or switch")


if stay == 'stay':
    final = pick
else:
    final = otherdoor

if final == car:
    print('The car is behind '+ car + ' you win!')
else:
    print('There is a goat behind'+ pick + ' you lose')
