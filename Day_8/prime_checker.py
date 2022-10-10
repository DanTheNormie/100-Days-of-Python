#Write your code below this line 👇

def prime_checker(number):
  isPrime = True
  i = 2
  while(i**2 <= number):
    if(number%i == 0):
      isPrime = False
    i += 1
  if isPrime :
    if(number==1):
      isPrime = False
      print("1 is neither prime not composite")
    elif(number < 1):
      print("Please enter only positive integers > 0")  
    else:
      print("It's a prime number")
  else:
    print("It's not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

