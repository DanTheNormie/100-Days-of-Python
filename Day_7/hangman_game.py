import random
import os
from Day_6.hangman_words import word_list
from Day_6.hangman_art import logo,stages

chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)


print(logo)

print('''
Rules :-

  (1) Player starts with 6 Lives.
  (2) Everytime the player makes a wrong guess or a duplicate guess,
        one part of the hangman figure is drawn.
       "Head" -> "Torso" -> "left hand" -> "right hand" -> "left leg" -> "right leg"
  (3) If you guess all the characters of the word without losing 6 lives, You win.
  (4) If the hangman figure is fully drawn, you lose.

  (5) Special case :- If you make 2 correct guesses in a row, you gain a life
''')

#print(f"The chosen word is : {chosen_word}")

game_finished = False
player_lives = 6
res_list =[]
for i in chosen_word :
    res_list+='_'
print("\n\n\n")
print(res_list)
print("\n")

last_guess = "wrong"
while(not game_finished):
  user_guess = input("Guess a letter : ")
  os.system('cls')
  guess_correct = False
  for i in range(len(chosen_word)):
    if(user_guess==chosen_word[i]):
      if(res_list[i] == '_'):
        res_list[i] = user_guess
        guess_correct = True

  if not guess_correct:
    last_guess = "wrong"
    player_lives -=1
    print(f"\nYou made a wrong guess, you lose a life. You now have {player_lives} lives\n")
  else:
    
    if(last_guess == "correct" and player_lives < 6):
      player_lives += 1
      print("!!!You guessed correctly back to back... You gain a life!!!")
    print("\nYou've made a correct guess, Keep going... Save The Hangman!!!\n")
    last_guess = "correct"

  print(res_list)
  print("\n")
  print(f"player lives = {player_lives}")
  print(stages[player_lives])
    
  if '_' not in res_list:
    game_finished = True
    print(" You won !!! You saved the hangman")
  elif player_lives < 1 :
    game_finished = True
    print("You Noob !!! You let the hangman hang.... booooo\n" )
    print(f"The word was {chosen_word}")