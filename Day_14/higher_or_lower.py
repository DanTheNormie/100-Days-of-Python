from Day_14.game_art import *
from Day_14.game_data import *
import os

def printCelebDetails(a):
  a_name = a["name"]
  a_desc = a["description"]
  a_from = a["country"]

  print(f"{a_name}, {a_desc} from {a_from}")

print(logo)

a = pickRandomCelebrity()
b = pickRandomCelebrity(a)

score = 0
msg = ""

while(True):
  print(f"\n\n{msg} Your score : {score}")
  
  ans = "1"
  a_count = a["follower_count"]
  b_count = b["follower_count"]
  if(a_count <= b_count):
    ans = "2"
  
  printCelebDetails(a)
  
  print(vs)
  
  printCelebDetails(b)
  user_input = input("Who has more followers ? type '1' or '2' : ")
  if(user_input == ans):
    msg = "You are correct !!!, You get a point."
    score+=1
  else:
    print("Sorry! That's Wrong :(")
    print(f"\nA has {a_count}m followers \nB has {b_count}m followers")
    
    break

  temp = pickRandomCelebrity(a)
  a = b
  b = temp

  os.system('cls')
  
print(f"\nYour Final score is : {score}")