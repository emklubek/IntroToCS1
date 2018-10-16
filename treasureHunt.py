#Treasure Hunt Game 
#10-11-2018

def main():
  difficulty = input("What difficulty do you want to play on? (easy, medium, or hard)")
  if difficulty == 'easy':
    easy()
  elif difficulty == 'medium':
    medium()
  elif difficulty == 'hard':
    hard()
  print("Thank you for finding my treasure! Have a gold coin for your troubles.")
  

def easy():
  turn = 7
  while turn >= 0:
    
def medium():
  turn = 9
  while turn >= 0:
  
def hard(): 
  turn = 11
  while turn >= 0:

#Greeting with a little bit of piracy
start = input("Welcome to the Treasure Hunt Game. \nAre you ready to hunt for some treasure?")
if start in ('Yes', 'yes', 'yeah', 'Yeah', 'ya', 'Ya'):
  print("Then let's hunt some treasure! Arg!")
else:
  print("That's to bad because you're going to find the treasure anyway.")

main()
