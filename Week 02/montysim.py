#Monty Hall Simulation - Patrick Moore 2018-10-02 - created for fun based on this problem https://en.wikipedia.org/wiki/Monty_Hall_problem
#The project is an attempt to create a simulator to test the different Monty Hall problem strategies
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns

# define a function for the simulation
def simulation(stay):

  # Set up the 3 doors and randomly put a car behind one of them, then randomly pick one
  doors = ['green', 'blue', 'red']
  car = np.random.choice(doors)
  pick = np.random.choice(doors)

  # Randomly choose a door to show (it can't be the one with the car or the original pick)
  show = np.random.choice([door for door in doors if door !=pick and door !=car])

  # Define what the door is that has not been picked or shown
  otherdoor = np.random.choice([door for door in doors if door !=pick and door !=show])

  # Define what the final answer is
  if stay == 'yes':
    final = pick
  elif stay == 'no':
    final = otherdoor

  # Check if they won and let them know
  if final == car:
    return('Win')
  else:
    return('Lose')

# Run the simulation 10,000 times with the person staying on the original pick
ls_stay = [simulation('yes') for i in range(10000)]

# Run the simulation 10,000 times with the person switching
ls_switch = [simulation('no') for i in range(10000)]

# Plot Results of Staying
ax = sns.countplot(y=ls_stay)
plt.title("Stay Simulation")
plt.show()

# Plot Results of Switching
ax = sns.countplot(y=ls_switch)
plt.title("Switch Simulation")
plt.show()




