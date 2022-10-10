from Day_10.calc_art import logo
import os
def compute(f_operand,operation,l_operand):
  result = 0
  if(operation == "+"):
    result = f_operand + l_operand
  elif(operation == "-"):
    result = f_operand - l_operand
  elif(operation == "*"):
    result = f_operand * l_operand
  else:
    result = f_operand / l_operand
  print(f"{f_operand} {operation} {l_operand} = {result}")
  return result


f_operand = 0.0
r = "n"
while(True):
  if(r == "n"):
    os.system('cls')
    print(logo)
    f_operand = float(input("What's your first number : "))
  print("\n+\n-\n*\n/")
  operation = input("pick an operation : ")
  print("")
  l_operand = float(input("What's your next number : "))

  result = compute(f_operand,operation,l_operand)

  r = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  f_operand = result






  
  
