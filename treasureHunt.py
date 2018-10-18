#Treasure Hunt Game 
#10-11-2018

import random
import pprint

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
  counter = 0
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  treasures = [' ', ' ', ' ', ' ', ' ']
  treasures[0] = random.randint(1,9)
  treasures[1] = random.randint(1,9)
  treasures[2] = random.randint(1,9)
  treasures[3] = random.randint(1,9)
  treasures[4] = random.randint(1,9)
  
  
  while turn >= 0:
    turn = turn - 1
    pprint.pprint(grid)
    guess = input("Where do ye want t' dig fer treasure? (Enter a number between 1 and 9)")
    if guess in treasures:
      counter = counter + 1
      if guess == 1:
        grid[0][0] = 'X'
      elif guess == 2:
        grid[0][1] = 'X'
      elif guess == 3:
        grid[0][2] = 'X'
      elif guess == 4:
        grid[1][0] = 'X'
      elif guess == 5:
        grid[1][1] = 'X'
      elif guess == 6:
        grid[1][2] = 'X'
      elif guess == 7:
        grid[2][0] = 'X'
      elif guess == 8:
        grid[2][1] = 'X'
      elif guess == 9:
        grid[2][2] = 'X'
     
      if counter < 5: 
        print("Thank ye for finding a treasure! Can ye find th' rest?")
      elif counter == 5:
        print("Thank ye fer finding all me treasure!")
    
    elif guess not in treasures:
      if guess == 1:
        grid[0][0] = 'O'
      if guess == 2:
        grid[0][1] = 'O'
      if guess == 3:
        grid[0][2] = 'O'
      if guess == 4:
        grid[1][0] = 'O'
      if guess == 5:
        grid[1][1] = 'O'
      if guess == 6:
        grid[1][2] = 'O'
      if guess == 7:
        grid[2][0] = 'O'
      if guess == 8:
        grid[2][1] = 'O'
      if guess == 9:
        grid[2][2] = 'O'
      print("Me treasure ain't there matey! Try Again.")
    print("You have", turn, "turns left")
  if counter < 5:
    print("Ye didn' find enough treasure.... Now ye must walk the plank. Argh!")
    

    
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
