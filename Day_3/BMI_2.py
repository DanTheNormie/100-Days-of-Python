print('Welcome to "BMI Calculator 2.0"') 
height = float(input("Enter your height in meters : "))
weight = float(input("Enter your wieght in kilograms : "))

bmi = weight / height**2
msg = "you are "
if(bmi<18.5):
  msg += "underweight"
elif(bmi<25):
  msg += "normal weight"
elif(bmi<30):
  msg += "over_weight"
elif(bmi<35):
  msg += "obese"
else:
  msg += "clinically obese"
        
print(f"Your BMI is {round(bmi,2)}, {msg}")