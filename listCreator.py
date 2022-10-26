import os
from typing import List
import random
import foodList

#add another function that stores the weekly list to a local variable and connect it to a reminder command so they list can be re-pasted in the server as requested.
#have that function call the ListCreator function so that it can be used for daily challenges and weekly ones.

#have an element in the general list that is just 'meat' or 'seafood' and if it is selected search the specific lists. have a local variable that is set to 1 or 0 and if
#'meat' or 'seafood' are selected switch to to the other value and have the corresponding value in the conditional so an extra one isnt added to the list for when it checks
#for matching values.

fullTuple = (foodList.foodTuple + foodList.meatTuple)

def ListCreator():
    ingredientList = []

    while(ingredientList.count < 3):
      randomchoice = random.choice(fullTuple)
      if(randomchoice  not in ingredientList):
        ingredientList.append(randomchoice)
    
    return ingredientList