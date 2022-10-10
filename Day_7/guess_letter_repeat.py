import random

word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print("-----Debug start-----")

print(f"Chosen word : {chosen_word}\n")

print("-----Debug end-----")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word 
game_finished = False

res_list =[]
for i in chosen_word :
    res_list+='_'

while(not game_finished):
  user_guess = input("Guess a letter : ")

  for i in range(len(chosen_word)):
    if(chosen_word[i]==user_guess):
      res_list[i] = user_guess

  print(res_list)

  if '_' not in res_list:
    game_finished = True
    print(" You won !!!")