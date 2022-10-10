import random
from Day_12.guess_num_art import logo

number = random.randint(0,100)

print(logo)


print("""Welcome to the Number Guessing Game !!!
I'm Thinking of a number between 1 and 100""")
no_of_attempts = 10
if(input("Choose a difficult. Type 'easy' or 'hard' : ") == "hard"):
  no_of_attempts = 5


should_loop = True
while(no_of_attempts > 0):
  print(f"You have {no_of_attempts} remaining to guess the number")
  
  guess = int(input("Guess a number : "))
  
  
  if(guess == number):
    should_loop = False
    
  elif(guess < number):
    print("Too low.\nGuess again.")
  elif(guess > number):
    print("Too high.\nGuess again.")
  no_of_attempts -= 1

if(no_of_attempts > 0):
  print(f"You've successfully guessed the number.\nYou Win. The number is {number}")
else:
  print(f"You've run out of attempts. You lose.\nThe number was {number}.")