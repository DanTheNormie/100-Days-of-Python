#Password Generator Project
import random

def generate():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the PyPassword Generator!")
  nr_char_not_set = True
  while(nr_char_not_set):
    nr_char = int(input("How many characters should your password be ? \n"))
    if(nr_char<1):
      print("Your password cannot be less than 1 character!!!\nWhat are you.. Dumb?")
    else:
      nr_char_not_set = False
  char_remaining = nr_char
  letters_not_set = True
  symbols_not_set = True
  numbers_not_set = True
  while(letters_not_set):
    nr_letters = int(input("ateast how many letters would you like in your password?\n"))
    
    if(char_remaining- nr_letters >= 0):
      letters_not_set = False
      char_remaining -= nr_letters
    else:
      print(f"You can't have that many letters!!! \n Valid range is between 0 and {char_remaining}")
  while(symbols_not_set):
    nr_symbols = int(input("ateast how many symbols would you like in your password?\n"))
  
    if(char_remaining-nr_symbols >= 0):
      symbols_not_set = False
      char_remaining -= nr_symbols
    else:
      print(f"You can't have that many symbols!!! \n Valid range is between 0 and {char_remaining}")
  while(numbers_not_set):
    nr_numbers = int(input("ateast how many numbers would you like in your password?\n"))

    if(char_remaining-nr_numbers >= 0):
      numbers_not_set = False
      char_remaining -= nr_numbers
    else:
      print(f"You can't have that many numbers!!! \n Valid range is between 0 and {char_remaining}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  print("\n\n------Debug Start------\n\n")
  print(f"total_char = {nr_char}")
  password = ""
  for i in range(0,nr_char):
  
    rand_char_index = random.randint(1,3)
    print(f"nr_letters = {nr_letters}")
    print(f"nr_symbols = {nr_symbols}")
    print(f"nr_numbers = {nr_numbers}")
    print(f"rand_char_index= {rand_char_index}")
    if(rand_char_index == 1):
      if(nr_letters>0):
        rand_letter = letters[random.randint(0,len(letters)-1)]
        print(f"rand_letter = {rand_letter}")
        password+=rand_letter
        nr_letters-=1
      elif(nr_symbols>0):
        rand_symbol = symbols[random.randint(0,len(symbols)-1)]
        print(f"rand_symbol = {rand_symbol}")
        password+=rand_symbol
        nr_symbols-=1
      elif(nr_numbers>0):
        rand_numb = numbers[random.randint(0,len(numbers)-1)]
        print(f"rand_numb = {rand_numb}")
        password+=rand_numb
        nr_numbers-=1
      else:
        rand_letter = letters[random.randint(0,len(letters)-1)]
        print(f"rand_letter = {rand_letter}")
        password+=rand_letter
        nr_letters-=1
    elif(rand_char_index == 2):
      if(nr_symbols>0):
          rand_symbol = symbols[random.randint(0,len(symbols)-1)]
          print(f"rand_symbol = {rand_symbol}")
          password+=rand_symbol
          nr_symbols-=1
      elif(nr_letters>0):
        rand_letter = letters[random.randint(0,len(letters)-1)]
        print(f"rand_letter = {rand_letter}")
        password+=rand_letter
        nr_letters-=1  
      elif(nr_numbers>0):
        rand_numb = numbers[random.randint(0,len(numbers)-1)]
        print(f"rand_numb = {rand_numb}")
        password+=rand_numb
        nr_numbers-=1
      else:
        rand_symbol = symbols[random.randint(0,len(symbols)-1)]
        print(f"rand_symbol = {rand_symbol}")
        password+=rand_symbol
        nr_symbols-=1
    elif(rand_char_index == 3):
      if(nr_numbers>0):
        rand_numb = numbers[random.randint(0,len(numbers)-1)]
        print(f"rand_numb = {rand_numb}")
        password+=rand_numb
        nr_numbers-=1
      elif(nr_symbols>0):
        rand_symbol = symbols[random.randint(0,len(symbols)-1)]
        print(f"rand_symbol = {rand_symbol}")
        password+=rand_symbol
        nr_symbols-=1
      elif(nr_letters>0):
        rand_letter = letters[random.randint(0,len(letters)-1)]
        print(f"rand_letter = {rand_letter}")
        password+=rand_letter
        nr_letters-=1  
      else:
        rand_numb = numbers[random.randint(0,len(numbers)-1)]
        print(f"rand_numb = {rand_numb}")
        password+=rand_numb
        nr_numbers-=1
    nr_char -= 1
  print("\n\n------Debug End------\n\n")
    
  print(f"\n\nRandom password is : {password}")
  