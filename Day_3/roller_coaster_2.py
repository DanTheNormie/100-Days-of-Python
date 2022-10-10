print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm ? :"))

if(height < 120):
  print("You can't ride the rollercoaster !")
else:
  print("You can ride the rollercoaster !")
  age = int(input("What's your age ? : "))
  total_bill = 0
  if(age<12):
    total_bill+=5
  elif(age<18):
    total_bill+=7
  else:
    total_bill+=12
  want_photos = input('Type "yes" if you want photos: ')
  if(want_photos == "yes"):
    total_bill+=3
  print(f"Your total bill is ${total_bill}")