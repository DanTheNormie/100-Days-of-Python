import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

user_guess = input("Guess a letter : ")


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in chosen_word:
  if(i==user_guess):
    print(f"{i} Right")
  else:
    print(f"{i} Wrong")

print("-----Debug start-----")

print(f"Chosen word : {chosen_word}\n")
print(f"Chosen character : {user_guess}")

print("-----Debug end-----")