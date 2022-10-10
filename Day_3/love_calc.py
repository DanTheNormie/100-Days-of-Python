print("Welcome to the Love_Calculator!")

name1 = input("What's your name ? :").lower()

name2 = input("What's your cursh's name ? :").lower()

total_name = name1+name2

t_count = total_name.count("t")
r_count = total_name.count("r")
u_count = total_name.count("u")
e_count = total_name.count("e")
op=t_count+r_count+u_count+e_count

l_count = total_name.count("l")
o_count = total_name.count("o")
v_count = total_name.count("v")
e_count = total_name.count("e")
opp=l_count+o_count+v_count+e_count

love_score = int(op+opp)

msg = f"Your love score is {love_score} %. "

if(love_score < 10 or love_score > 90):
  msg+="You guys go together like coke and mentos."
elif(love_score>=40 or love_score<=50):
  msg+="You guys are alright."

print(msg)