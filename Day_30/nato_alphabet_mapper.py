import pandas

nato_dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_dataFrame.iterrows()}

string_is_not_proper = True
while string_is_not_proper:

    user_input = input("Enter any string : ")
    try:
        code_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, Only letters in alphabet please.")
    else:
        string_is_not_proper = False

print(code_list)
