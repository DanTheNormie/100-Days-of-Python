import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


user_guess = input("Guess a letter : ")




for i in chosen_word:
  if(i==user_guess):
    print(f"{i} Right")
  else:
    print(f"{i} Wrong")

print("-----Debug start-----")

print(f"Chosen word : {chosen_word}\n")
print(f"Chosen character : {user_guess}")

print("-----Debug end-----")