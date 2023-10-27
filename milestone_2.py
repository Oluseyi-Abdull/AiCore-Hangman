#Task_2 COMPLETED
import random

word_list = ["pineapple","mango","strawberry","watermelon","banana"]

#Added try excepts to handle error when list is not entered into the function. 
def choice(fruits):
  if type(fruits) == list:
    try:
      print(random.choice(fruits)) # This is for testing purposes 
    except:
      raise TypeError("The values entered into the choice method must be of list Type")
  return

word = choice(word_list)
word
# #In this step a method is created to grab a random fruit from the 
# list of the fruitsthat are my favourite
