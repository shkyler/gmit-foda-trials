#Monty Hall Game - Patrick Moore 2018-10-02 - created for fun based on this problem https://en.wikipedia.org/wiki/Monty_Hall_problem
import numpy as np 

# Set up the 3 doors and randomly put a car behind one of them
doors = ['green', 'blue', 'red']
car = np.random.choice(doors)

# ask the user for the initial pick - value entered must be valid
print('There is a car behind one of the doors, please pick red, green or blue')
pick = input('Please pick a door!')
while pick not in doors:
    pick = input("Please pick a valid door!")

# Randomly choose a door to open (it can't be the one with the car or the original pick)
show = np.random.choice([door for door in doors if door !=pick and door !=car])
print("I can now reveal to you that there is no car behind the " + show + " door")

# Define what the door is that has not been picked or showed
otherdoor = np.random.choice([door for door in doors if door !=pick and door !=show])

# Ask the user would they like to stay or switch - value entered must be valid
stay = input("Would you like to stay with your original door or switch?")
while stay not in ['stay', 'switch']:
    stay = input ("Would you like to stay or switch")

# Define what the final answer is
if stay == 'stay':
    final = pick
else:
    final = otherdoor

# Check if they won and let them know
if final == car:
    print('The car is behind '+ car + ' you win!')
else:
    print('There is a goat behind '+ pick + ' you lose')
