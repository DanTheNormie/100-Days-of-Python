import pandas

nato_dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_dataFrame.iterrows()}

user_input = input("Enter any string : ")

code_list = [nato_dict[letter.upper()] for letter in user_input]

print(code_list)
