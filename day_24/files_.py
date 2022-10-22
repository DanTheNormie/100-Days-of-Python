with open("../../../Desktop/new_file.txt", mode="a") as file:
    file.write(f"\nNew File\n")

with open("../../../Desktop/new_file.txt") as file:
    print(file.read())
