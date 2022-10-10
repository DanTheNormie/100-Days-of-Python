print("Welcome to the tip calculator")

bill = float(input("What was the total bill ? : "))

tip_percentage = int( input("What percentage of tip would you like to give ? : "))

no_of_people_to_split = int(input("How many people to split the bill? : "))

total_bill = bill + (bill*(tip_percentage/100))

divided_bill = total_bill/no_of_people_to_split

print(f"Each person should pay : ${round(divided_bill,2)}")