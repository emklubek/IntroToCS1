#Treasure Hunt Game 
#10-11-2018

import random

#main part of the program with difficulty selection and function calling
def main():
  difficulty = input("What difficulty do you want to play on? (easy, medium, or hard)")
  if difficulty == 'easy':
    easy()
  elif difficulty == 'medium':
    medium()
  elif difficulty == 'hard':
    hard()
  print("Thank ye fer findin' me loot! 'ave a gold shillin' fer yer troubles.")
  

def easy():
  turn = 7
  grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  treasures = [' ', ' ', ' ', ' ', ' ']
  for i in range(1,5):
    random_num = random.randint(1,9)
  treasures.i
  
  while turn >= 0:
    print(grid)
    guess = input("Where do ye want t' dig fer treasure? (Enter a number between 1 and 9)")
    if guess in treasures:
      print("Thank ye for finding me treasure!")
    elif:
      print("Me treasure ain't there matey! Try Again.")
    turn = turn - 1
    

    
def medium():
  turn = 9
  grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  treasures = [' ', ' ', ' ', ' ', ' ']
  while turn >= 0:
    
  

  
def hard(): 
  turn = 11
  grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  treasures = [' ', ' ', ' ', ' ', ' ']
  while turn >= 0:
    

#Greeting with a little bit of piracy
start = input("Ahoy! Welcome to the Treasure Hunt Game. \nAre you ready to hunt fer some treasure?")
if start in ('Yes', 'yes', 'yeah', 'Yeah', 'ya', 'Ya'):
  print("Then let's hunt fer some treasure! Arg!")
else:
  print("That's t' bad 'cause ye're goin' t' find me treasure anyway.")

  
  #executing program with call of main
main()
