from Day_10.calc_art import logo
import os

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


r="n"
while(True):
  
  if(r=="n"):
    print(logo)
    num1 =  float(input("What's your first number : "))

  for key in operations :
    print(key)

  operation = input("Pick an operation from one of the above : ")

  num2 = float(input("What's your next number : "))

  result = operations[operation](num1,num2)

  print(f"{num1} {operation} {num2} = {result}")

  r = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  num1 = result