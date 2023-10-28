import random

word_list = ["pineapple","mango","strawberry","watermelon","banana"]

#Creating the Hangman Class and its necessary methods for the game to run.
class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
      self.list_letters = []  
      self.word = random.choice(word_list)
      self.word_guessed = list('_' * len(self.word))
      self.num_letters = len(set(list(self.word)))
      self.num_lives = num_lives
    
      print(f"The mistery word has {self.num_letters} characters")
      print(f"{self.word_guessed}")

    def ask_letter(self): # Requesting an imput from the user to ensure 
      letter = input("Please enter a letter: ")
      if letter.isalpha() != True:
        print("Please, enter an alphabetical character") # Ensuring it is an alphabetical 
      elif len(letter) != 1:
          print("Please, enter just one character")
      elif letter in self.list_letters:
          print(f"{letter} was already tried")
      else:
          self.check_letter(letter)

    def check_letter(self, letter) -> None: # Function being used to check the entered characters 
      letter = letter.lower()
      if letter in self.word:
          print(f"The letter {letter} is in the word to be guessed!")
          letter_index = 0
          for position, char in enumerate(self.word):
              if char == letter:
                  letter_index = position
                  self.word_guessed[letter_index] = letter
          print(f"Nice! {letter} is in the word!")
          print(f"{self.word_guessed}")
          self.num_letters -= 1
      else:
          self.num_lives -= 1 # Also making sure incorrect guesses remove lives
          print(f"Sorry, {letter} is not in the word.")
          print(f"{[self.num_lives]}")
          print(f"You have {self.num_lives} lives left.")
      self.list_letters.append(letter)

def play(word_list): # Function to play the game 
  game_play = Hangman(word_list, num_lives=5)
  while True:
      if game_play.num_lives == 0:
          print(f"You lost, The word was {game_play.word} >:[]")
          break
      elif game_play.num_letters > 0:
          game_play.ask_letter()
      else:
          print("Congratulations! You have won!")
          break

if __name__ == '__main__':
    play(word_list)
