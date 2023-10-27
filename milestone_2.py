#Task_1 and Task_2 
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

#Task_3 and 4
guess = input("Please Enter a single letter guess: ")
if len(guess) == 1:
    print("Good guess!.")
else:
  #could use try except block and raise a value error instead. 
    print("Oops! That is not a valud input.")
