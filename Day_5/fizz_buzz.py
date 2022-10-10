three_counter = 0
five_counter = 0
msg = ""

for i in range(1,101):
    three_counter += 1
    five_counter  += 1
    if(three_counter == 3):
        msg += "Fizz"
        three_counter= 0
    if(five_counter == 5):
        msg += "Buzz"
        five_counter = 0
    if(len(msg)==0):
        print(i)
    else:
        print(msg)
        msg = ""
    