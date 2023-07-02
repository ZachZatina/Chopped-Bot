import os
from typing import List
import random
import foodList

#add another function that stores the weekly list to a local variable and connect it to a reminder command so they list can be re-pasted in the server as requested.
#have that function call the ListCreator function so that it can be used for daily challenges and weekly ones.

#have an element in the general list that is just 'meat' or 'seafood' and if it is selected search the specific lists. have a local variable that is set to 1 or 0 and if
#'meat' or 'seafood' are selected switch to to the other value and have the corresponding value in the conditional so an extra one isnt added to the list for when it checks
#for matching values.

def ListCreator():
    ingredientList = []
    
    meatcount = 0
    liquidcount = 0

    while(len(ingredientList) < 3):
      randomnum = random.randrange(1, 101)

      if ( randomnum <= 65 ):
         randomchoice = random.choice(foodList.foodTuple)
         if (randomchoice  not in ingredientList):
          ingredientList.append(randomchoice)
      elif ( randomnum > 65 and randomnum <= 92 and meatcount == 0):
         meatcount = meatcount + 1
         randomchoice = random.choice(foodList.meatTuple + foodList.seafoodTuple)
         if (randomchoice  not in ingredientList):
          ingredientList.append(randomchoice)
      elif ( randomnum > 92 and liquidcount == 0):
         liquidcount = liquidcount + 1
         randomchoice = random.choice(foodList.liquidTuple)
         if (randomchoice  not in ingredientList):
          ingredientList.append(randomchoice)
      else:
        continue

    return ingredientList