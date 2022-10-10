import os
from Day_8.caesar_cypher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def en_de_crypt(text,shift,direction):
  e_text = ""
  if(direction == "decode"):
    shift *= -1
  for i in text:
    ab_index = alphabet.index(i)
    actual_index = ((ab_index+shift)%26)
    e_text += alphabet[actual_index]
    
  print(f"The {direction}d text is {e_text}")

re_run = True

print(logo)

while(re_run):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift number: "))

  en_de_crypt(text,shift,direction)

  rerun = input("Do you want to go again ? type yes/no : ").lower()

  if(rerun == "no"):
    re_run = False
    print("Goodbye")
  else:
    os.system('cls')
