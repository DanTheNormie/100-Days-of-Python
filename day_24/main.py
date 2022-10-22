with open("./Input/Letters/starting_letter.txt",mode="r") as file:
    letter_template = file.read()

with open("./Input/Names/invited_names.txt",mode="r") as file:
    names_string = file.read()

    names_list = names_string.split("\n")

    for name in names_list:
        personalized_letter = letter_template.replace("[name]",name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(personalized_letter)