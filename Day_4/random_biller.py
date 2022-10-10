import random

test_seed = random.randint(0,5000)
random.seed(test_seed)


names = input("Type everyone's names seperated by a comma. \n")

names_list = names.split(", ")


ran_int = random.randint(0,len(names_list)-1)

print(f"{names_list[ran_int]} is going to buy the meal today!")