import random

test_seed = random.randint(0,5000)
random.seed(test_seed)

ran_int = random.randint(0,1)

if(ran_int == 0):
  print("Heads")
else:
  print("Tails")