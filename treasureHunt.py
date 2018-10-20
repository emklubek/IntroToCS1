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
  elif difficulty not in ('easy', 'medium', 'hard'):
    print("Oops, that is not an option. Please try again.")
    main() 

#easy setting of game
def easy():
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  turn = 7
  counter = 0
  treasures = []
  count = 0
  while count != 5:
    num = random.randint(1,9)
    if num not in treasures:
      count = count + 1
      treasures.append(num)
  
  while turn > 0:
   
    turn = turn - 1
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]))
    guess = int(input("Where do ye want t' dig fer treasure? (Enter a number between 1 and 9)"))
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
        print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]))
        print("Thank ye fer finding all me treasure!")
        return
    elif guess not in treasures:
      if guess == 1:
        grid[0][0] = 'O'
      elif guess == 2:
        grid[0][1] = 'O'
      elif guess == 3:
        grid[0][2] = 'O'
      elif guess == 4:
        grid[1][0] = 'O'
      elif guess == 5:
        grid[1][1] = 'O'
      elif guess == 6:
        grid[1][2] = 'O'
      elif guess == 7:
        grid[2][0] = 'O'
      elif guess == 8:
        grid[2][1] = 'O'
      elif guess == 9:
        grid[2][2] = 'O'
      print("Me treasure ain't there matey! Try Again.")
    print("You have", turn, "turn(s) left")
  if counter < 5:
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]))
    print("Ye didn' find enough treasure.... Now ye must walk the plank. Argh!")
    
#medium setting of game
def medium():
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  turn = 9
  counter = 0
  treasures = []
  count = 0
  while count != 5:
    num = random.randint(1,12)
    if num not in treasures:
      count = count + 1
      treasures.append(num)
  
  while turn > 0:
   
    turn = turn - 1
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]))
    guess = int(input("Where do ye want t' dig fer treasure? (Enter a number between 1 and 12)"))
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
      elif guess == 10:
        grid[3][0] = 'X'
      elif guess == 11:
        grid[3][1] = 'X'
      elif guess == 12:
        grid[3][2] = 'X'

      if counter < 5: 
        print("Thank ye for finding a treasure! Can ye find th' rest?")
      elif counter == 5:
        print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]))
        print("Thank ye fer finding all me treasure!")
        return
    elif guess not in treasures:
      if guess == 1:
        grid[0][0] = 'O'
      elif guess == 2:
        grid[0][1] = 'O'
      elif guess == 3:
        grid[0][2] = 'O'
      elif guess == 4:
        grid[1][0] = 'O'
      elif guess == 5:
        grid[1][1] = 'O'
      elif guess == 6:
        grid[1][2] = 'O'
      elif guess == 7:
        grid[2][0] = 'O'
      elif guess == 8:
        grid[2][1] = 'O'
      elif guess == 9:
        grid[2][2] = 'O'
      elif guess == 10:
        grid[3][0] = 'O'
      elif guess == 11:
        grid[3][1] = 'O'
      elif guess == 12:
        grid[3][2] = 'O'
      print("Me treasure ain't there matey! Try Again.")
    print("You have", turn, "turn(s) left")
  if counter < 5:
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]))
    print("Ye didn' find enough treasure.... Now ye must walk the plank. Argh!")
    
#hard setting of game
def hard():
  grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  turn = 11
  counter = 0
  treasures = []
  count = 0
  while count != 5:
    num = random.randint(1,15)
    if num not in treasures:
      count = count + 1
      treasures.append(num)
  
  while turn > 0:
   
    turn = turn - 1
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]), '\n', (grid[4]))
    guess = int(input("Where do ye want t' dig fer treasure? (Enter a number between 1 and 15)"))
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
      elif guess == 10:
        grid[3][0] = 'X'
      elif guess == 11:
        grid[3][1] = 'X'
      elif guess == 12:
        grid[3][2] = 'X'
      elif guess == 13:
        grid[4][0] = 'X'
      elif guess == 14:
        grid[4][1] = 'X'
      elif guess == 15:
        grid[4][2] = 'X'

      if counter < 5: 
        print("Thank ye for finding a treasure! Can ye find th' rest?")
      elif counter == 5:
        print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]), '\n', (grid[4]))
        print("Thank ye fer finding all me treasure!")
        return
    elif guess not in treasures:
      if guess == 1:
        grid[0][0] = 'O'
      elif guess == 2:
        grid[0][1] = 'O'
      elif guess == 3:
        grid[0][2] = 'O'
      elif guess == 4:
        grid[1][0] = 'O'
      elif guess == 5:
        grid[1][1] = 'O'
      elif guess == 6:
        grid[1][2] = 'O'
      elif guess == 7:
        grid[2][0] = 'O'
      elif guess == 8:
        grid[2][1] = 'O'
      elif guess == 9:
        grid[2][2] = 'O'
      elif guess == 10:
        grid[3][0] = 'O'
      elif guess == 11:
        grid[3][1] = 'O'
      elif guess == 12:
        grid[3][2] = 'O'
      elif guess == 13:
        grid[4][0] = 'O'
      elif guess == 14:
        grid[4][1] = 'O'
      elif guess == 15:
        grid[4][2] = 'O'
      print("Me treasure ain't there matey! Try Again.")
    print("You have", turn, "turn(s) left")
  if counter < 5:
    print('', (grid[0]), '\n', (grid[1]), '\n', (grid[2]), '\n', (grid[3]), '\n', (grid[4]))
    print("Ye didn' find enough treasure.... Now ye must walk the plank. Argh!")
    
    

#Greeting with a little bit of piracy
start = input("Ahoy! Welcome to the Treasure Hunt Game. \nAre you ready to hunt fer some treasure?")
if start in ('Yes', 'yes', 'yeah', 'Yeah', 'ya', 'Ya'):
  print("Then let's hunt fer some treasure! Arg!")
else:
  print("That's t' bad 'cause ye're goin' t' find me treasure anyway.")

  
  #executing program with call of main
main()
