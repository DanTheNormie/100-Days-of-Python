print('Welcome to "Leap year or not"')

year = int(input("Enter a year : "))

msg = ""
if(year%4==0):
  if(year%100==0):
    if(year%400!=0):
      msg = "not "
else:
  msg = "not "
  
print(f"This is {msg}a leap year !")
